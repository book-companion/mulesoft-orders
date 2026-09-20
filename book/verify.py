#!/usr/bin/env python3
"""HTTP contract checks for one deployed checkpoint. Uses synthetic local state."""
import argparse
import json
import urllib.error
import urllib.request
from pathlib import Path

BOOK = Path(__file__).resolve().parent
BASE = "http://127.0.0.1:18881"
STUB = "http://127.0.0.1:18882"
RECORDS = []
ORDER = json.loads((BOOK / "fixtures/order-calculation.json").read_text())
COMMAND = json.loads((BOOK / "fixtures/order-command.json").read_text())


def call(path, data=None, method=None, base=BASE, headers=None):
    raw = None if data is None else json.dumps(data).encode()
    request = urllib.request.Request(base + path, data=raw, method=method,
                                    headers={"Content-Type": "application/json", **(headers or {})})
    try:
        response = urllib.request.urlopen(request, timeout=20)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        body = response.read().decode()
        try:
            value = json.loads(body)
        except ValueError:
            value = body
        return response.status, value


def check(name, path, expected, data=None, status=200, method=None, base=BASE, headers=None):
    actual_status, actual = call(path, data, method, base, headers)
    RECORDS.append({"name": name, "status": actual_status, "actual": actual,
                    "expectedStatus": status, "expected": expected})
    assert actual_status == status and actual == expected, RECORDS[-1]
    print("PASS", name, flush=True)
    return actual


def basic(chapter):
    check("hello", "/hello", "Hello, Mule!")
    if chapter == 2:
        check("request-path", "/inspect/A-1001", "A-1001", ORDER)
        check("response-replaced", "/replace", "Request received", ORDER)
    elif chapter == 3:
        check("order-header", "/header", {"reference": "A-1001", "buyer": "Dana"}, ORDER)
        check("one-line", "/line", {"lineTotal": 10}, {"price": 2.5, "qty": 4})
        check("text-price", "/line/text", {"lineTotal": 10}, {"price": "2.5", "qty": 4})
    elif chapter in (4, 5, 6):
        check("order-total", "/summary", {"orderId": "A-1001", "total": 32}, ORDER)
        check("empty-total", "/summary", {"orderId": "EMPTY", "total": 0}, {"orderId": "EMPTY", "items": []})
        if chapter == 4:
            check("line-totals", "/lines", [{"sku": "PEN-01", "lineTotal": 10}, {"sku": "PAD-22", "lineTotal": 12}, {"sku": "CLP-08", "lineTotal": 10}], ORDER)
        else:
            check("retained-id", "/context", {"orderId": "A-1001", "lookup": "lookup complete"}, ORDER)
            check("subflow-total", "/total", {"orderId": "A-1001", "total": 32}, ORDER)
            check("target-restores", "/target", {"payload": "before", "stage": "caller", "result": "after"})
    elif chapter in (7, 8):
        check("valid-order", "/validate", {"orderId": "A-1001", "valid": True}, ORDER)
        for label, value in [("missing-items", {"orderId": "A-1001"}), ("empty-items", {"orderId": "A-1001", "items": []}), ("negative-quantity", {"orderId": "A-1001", "items": [{"qty": -1}]}), ("fractional-quantity", {"orderId": "A-1001", "items": [{"qty": 1.5}]})]:
            check(label, "/validate", {"error": "INVALID_ORDER"}, value, status=400)
        if chapter == 8:
            check("continue-owner", "/optional", {"result": "fallback", "reachedAfterTry": True})
    elif chapter == 9:
        check("customer-response", "/customer", {"id": "C-42", "name": "Dana", "status": "ACTIVE"})
    elif chapter == 10:
        check("enrichment", "/enriched", {"orderId": "A-1001", "customer": "Dana", "status": "ACTIVE"}, ORDER)
        check("optional-fallback", "/shipping", {"orderId": "A-1001", "shipping": {"available": False}}, ORDER)
    elif chapter in (11, 12):
        check("isolated-reset", "/lab/setup", "ready", {})
        check("insert", "/lab/orders", {"orderId": "A-1001", "affectedRows": 1}, {"orderId": "A-1001", "customer": "Dana", "total": 32})
        check("read-back", "/lab/orders/A-1001", [{"orderId": "A-1001", "customer": "Dana", "total": 32}])
        check("absent-row", "/lab/orders/ABSENT", [])
        if chapter == 12:
            check("rollback-response", "/lab/rollback", "rolled back", {})
            check("rollback-state", "/lab/orders/ROLLBACK", [])
            check("continue-response", "/lab/continue", "handled inside", {})
            check("continue-state", "/lab/orders/CONTINUE-INNER", [{"orderId": "CONTINUE-INNER", "customer": "Dana", "total": 32}])
    elif chapter == 13:
        check("contract-preview", "/api/orders", {"orderId": "A-1001", "state": "PREVIEW"}, COMMAND, status=201)
        check("not-persisted", "/api/orders/A-1001", {"error": "NOT_FOUND"}, status=404)
        contract_cases()
    elif chapter == 14:
        check("reset-api", "/lab/setup", "ready", {})
        expected = {"orderId": "A-1001", "tenantId": "retailer-a", "currency": "USD",
                    "items": [{"sku": "PEN-01", "qty": 4, "unitPrice": 2.5, "lineTotal": 10},
                              {"sku": "PAD-22", "qty": 2, "unitPrice": 6, "lineTotal": 12},
                              {"sku": "CLP-08", "qty": 10, "unitPrice": 1, "lineTotal": 10}],
                    "total": 32, "state": "ACCEPTED"}
        check("create-persisted-order", "/api/orders", expected, COMMAND, status=201)
        check("retrieve-created-order", "/api/orders/A-1001", expected)
        check("duplicate-conflict", "/api/orders", {"error": "ORDER_CONFLICT"}, COMMAND, status=409)
        check("unknown-order", "/api/orders/ABSENT", {"error": "NOT_FOUND"}, status=404)
        contract_cases()


def contract_cases():
    _, before = call("/control/state", base=STUB)
    for name, data in [("empty-command", {}), ("empty-command-items", {"orderId": "EMPTY", "items": []}),
                       ("reject-client-price", {"orderId": "PRICE", "items": [{"sku": "PEN-01", "qty": 1, "price": 0.01}]}),
                       ("unknown-product", {"orderId": "UNKNOWN", "items": [{"sku": "NO-SUCH-SKU", "qty": 1}]})]:
        check(name, "/api/orders", {"error": "INVALID_REQUEST"}, data, status=400)

    _, after = call("/control/state", base=STUB)
    assert before['calls'] == after['calls'], (before, after)
    RECORDS.append({'name': 'rejected-input-no-dependency-call', 'callsUnchanged': True})


def expected_order(order_id='A-1001', tenant='retailer-a'):
    return {'orderId': order_id, 'tenantId': tenant, 'currency': 'USD',
            'items': [{'sku': 'PEN-01', 'qty': 4, 'unitPrice': 2.5, 'lineTotal': 10},
                      {'sku': 'PAD-22', 'qty': 2, 'unitPrice': 6, 'lineTotal': 12},
                      {'sku': 'CLP-08', 'qty': 10, 'unitPrice': 1, 'lineTotal': 10}],
            'total': 32, 'state': 'ACCEPTED'}


def eventually(path, expected):
    import time
    for _ in range(60):
        status, actual = call(path)
        if status == 200 and actual == expected:
            return check('completed-' + path, path, expected)
        time.sleep(0.5)
    raise AssertionError((path, status, actual, expected))


def advanced(chapter):
    check('hello', '/hello', 'Hello, Mule!')
    if chapter == 15:
        check('file-roundtrip', '/lab/file', {'orderId': 'A-1001', 'file': 'order.json'}, ORDER)
        check('csv-normalized', '/lab/csv', [{'sku': 'PEN-01', 'price': 2.5, 'qty': 4}, {'sku': 'PAD-22', 'price': 6, 'qty': 2}, {'sku': 'CLP-08', 'price': 1, 'qty': 10}])
    if chapter == 16:
        records = json.loads((BOOK / 'fixtures/import-records.json').read_text())
        outcomes = [{'orderId': 'IMPORT-1', 'status': 'processed'}, {'orderId': 'IMPORT-2', 'status': 'rejected'}, {'orderId': 'IMPORT-3', 'status': 'processed'}]
        check('sequential-outcomes', '/lab/import', outcomes, records)
        eventually('/lab/scheduled', outcomes)
    if chapter == 17:
        check('parallel-lookups', '/lab/parallel-lookups', {'customer': 'Dana', 'prices': {'PEN-01': 2.5, 'PAD-22': 6, 'CLP-08': 1}})
        check('parallel-items', '/lab/parallel-items', [2, 4, 6])
        check('composite-failure', '/lab/parallel-failure', {'error': 'DEPENDENCY_ROUTE_FAILED'}, status=502)
    if chapter >= 18:
        check('reset-api', '/lab/setup', 'ready', {})
        check('first-acceptance', '/api/orders', expected_order(), COMMAND, status=201)
        check('replayed-result', '/api/orders', expected_order(), COMMAND)
        changed = {**COMMAND, 'items': [{'sku': 'PEN-01', 'qty': 9}]}
        check('conflicting-replay', '/api/orders', {'error': 'ORDER_CONFLICT'}, changed, status=409)
        check('stored-result', '/api/orders/A-1001', expected_order())
        rejected = {**COMMAND, 'orderId': 'FAIL-ORDER'}
        check('injected-transaction-failure', '/lab/accept-failure', {'error': 'INJECTED_FAILURE'}, rejected, status=500)
        check('no-partial-order', '/api/orders/FAIL-ORDER', {'error': 'NOT_FOUND'}, status=404)
        check('retry-after-rollback', '/api/orders', expected_order('FAIL-ORDER'), rejected, status=201)
        from concurrent.futures import ThreadPoolExecutor
        race = {**COMMAND, 'orderId': 'RACE-ORDER'}
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda _: call('/api/orders', race), range(4)))
        assert sorted(status for status, body in results) == [200, 200, 200, 201], results
        assert all(body == expected_order('RACE-ORDER') for status, body in results), results
        RECORDS.append({'name': 'concurrent-same-key', 'statuses': sorted(status for status, body in results), 'responsesMatch': True})
        print('PASS concurrent-same-key', flush=True)
        if chapter == 18:
            check('reset-dependencies', '/control/reset', {'reset': True}, {}, base=STUB)
            call('/control', {'failNext': 2}, base=STUB)
            check('bounded-retry', '/lab/retry', {'available': True})
            status, state = call('/control/state', base=STUB)
            assert state['calls']['/flaky'] == 3, state
            RECORDS.append({'name': 'retry-attempt-count', 'attempts': 3})
    if chapter >= 19:
        check('reset-outbox', '/lab/setup', 'ready', {})
        check('reset-receiver', '/control/reset', {'reset': True}, {}, base=STUB)
        check('accept-with-event', '/api/orders', expected_order(), COMMAND, status=201)
        check('committed-intent', '/lab/state', {'orders': 1, 'requests': 1, 'pending': 1})
        call('/control', {'loseResponseNext': True}, base=STUB)
        check('uncertain-publication', '/lab/dispatch', {'error': 'PUBLICATION_UNCERTAIN'}, {}, status=503)
        check('intent-still-pending', '/lab/state', {'orders': 1, 'requests': 1, 'pending': 1})
        status, receiver = call('/control/state', base=STUB)
        assert receiver['effects'] == 1, receiver
        check('repeat-publication', '/lab/dispatch', {'attempted': 1}, {})
        check('intent-completed', '/lab/state', {'orders': 1, 'requests': 1, 'pending': 0})
        status, receiver = call('/control/state', base=STUB)
        assert receiver['effects'] == 1 and receiver['calls']['/events'] == 2, receiver
        RECORDS.append({'name': 'two-deliveries-one-effect', 'deliveries': 2, 'effects': 1})
        print('PASS two-deliveries-one-effect', flush=True)
        check('empty-dispatch', '/lab/dispatch', {'attempted': 0}, {})
    if chapter == 20:
        import uuid
        notice = {'orderId': 'VM-' + str(uuid.uuid4())}
        check('transient-enqueue', '/lab/notices', {'queuedLocally': True}, notice, status=202)
        eventually('/lab/notices', notice)
        check('async-start', '/lab/async', {'startedLocally': True}, {})
    if chapter == 21:
        check('prepare-import', '/lab/import/setup', 'ready', {})
        records = json.loads((BOOK / 'fixtures/import-records.json').read_text())
        check('start-batch', '/lab/batch', {'started': True}, records, status=202)
        eventually('/lab/import/outcomes', [{'orderId': 'IMPORT-1', 'status': 'processed'}, {'orderId': 'IMPORT-2', 'status': 'rejected'}, {'orderId': 'IMPORT-3', 'status': 'processed'}])
    if chapter == 22:
        check('reset-cache-counter', '/control/reset', {'reset': True}, {}, base=STUB)
        check('clear-local-cache', '/lab/cache', {'invalidated': True}, method='DELETE')
        prices = {'PEN-01': 2.5, 'PAD-22': 6, 'CLP-08': 1}
        check('tenant-a-miss', '/lab/catalogue/retailer-a', prices)
        check('tenant-a-hit', '/lab/catalogue/retailer-a', prices)
        check('tenant-b-separate', '/lab/catalogue/retailer-b', {**prices, 'PEN-01': 3})
        status, state = call('/control/state', base=STUB)
        assert state['calls']['/catalogue'] == 2, state
        check('invalidate-one-key', '/lab/cache/retailer-a', {'invalidated': True}, method='DELETE')
        check('tenant-a-refetched', '/lab/catalogue/retailer-a', prices)
        status, state = call('/control/state', base=STUB)
        assert state['calls']['/catalogue'] == 3, state
        RECORDS.append({'name': 'cache-source-call-counts', 'beforeInvalidation': 2, 'afterInvalidation': 3})
        check('store-retrieve', '/lab/store', {'note': 'synthetic'}, {'note': 'synthetic'})

    if chapter in (23, 26, 30):
        check('other-tenant-cannot-read', '/lab/tenant-b/orders/A-1001', {'error': 'NOT_FOUND'}, status=404)
        check('missing-principal-rejected', '/lab/anonymous', {'error': 'UNAUTHENTICATED'}, status=401)
        contract_cases()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter", type=int)
    args = parser.parse_args()
    if args.chapter not in [*range(1,24),26,30]:
        parser.error("Unsupported checkpoint")
    try:
        if args.chapter <= 14:
            basic(args.chapter)
        else:
            advanced(args.chapter)
    finally:
        output = BOOK / "actual"
        output.mkdir(exist_ok=True)
        (output / f"chapter-{args.chapter:02d}.json").write_text(json.dumps(RECORDS, indent=2) + "\n")
    print(f"{len(RECORDS)} HTTP checks passed for chapter {args.chapter:02d}")


if __name__ == "__main__":
    main()
