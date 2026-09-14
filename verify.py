#!/usr/bin/env python3
"""Assert local synthetic fixtures only; no platform credentials or cloud calls."""
import json, pathlib, urllib.request
BASE = "http://127.0.0.1:18081"
OUT = pathlib.Path(__file__).with_name("results")
OUT.mkdir(exist_ok=True)
def check(name, path, expected, data=None):
    raw = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request(BASE+path, data=raw, headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        body=response.read().decode()
        actual=json.loads(body) if "application/json" in response.headers.get("Content-Type", "") else body
        record={"status":response.status,"actual":actual,"expected":expected}
    (OUT/(name+".json")).write_text(json.dumps(record,indent=2)+"\n")
    assert record["status"]==200 and actual==expected, (name,record)
    print("PASS",name)
check("hello","/hello","Hello, Mule!")
check("summary","/orders",{"id":"A-1001","total":32},{"orderId":"A-1001","items":[{"price":12.5,"qty":2},{"price":7,"qty":1}]})
check("setup","/lab/db/setup","ready",{})
check("insert","/lab/db/orders",{"order":"A-VERIFY","result":{"generatedKeys":{},"affectedRows":1}},{"orderId":"A-VERIFY","customer":"Dana","total":32})
check("select","/lab/db/orders/A-VERIFY",[{"id":"A-VERIFY","customer":"Dana","total":32}])
check("rollback","/lab/db/rollback","rolled back")
check("rollback-absent","/lab/db/orders/ROLLBACK",[])
check("file","/lab/files",{"orderId":"A-1001","path":"order.json"},{"orderId":"A-1001","customer":"Dana","total":32})
check("deferred","/lab/deferred",[{"id":"A-1001","total":32},{"id":"A-1002","total":7.5}],[{"orderId":"A-1001","total":32},{"orderId":"A-1002","total":7.5}])
check("flowref-target","/lab/target",{"payload":"before","marker":"original","result":"after"})
check("scatter-gather","/lab/routes",{"first":"inventory","second":"customer"})
check("parallel-foreach","/lab/parallel",[2,4,6])
check("java","/lab/java",{"integerClass":"java.lang.Integer","decimalClass":"java.lang.Double"})
check("xlsx","/lab/xlsx",{"Orders":[{"id":"A-1001","total":32}]})
check("flatfile","/lab/flatfile",[{"amountCents":12950,"customerId":"4021","name":"Dana Lopez"},{"amountCents":4999,"customerId":"4022","name":"Sam Okafor"}])
print("15 local assertions passed")
