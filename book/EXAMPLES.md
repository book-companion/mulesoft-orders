# Examples in reading order

Numbers are display order; slugs are stable identities. See [verification](verification/2026-09-20.md) for scope.

| Example | Chapter | Name / identity | Complete source | Evidence |
| --- | --- | --- | --- | --- |
| 001 | 1 | Hello Mule / `hello-mule` | [checkpoints/01-hello/src/main/mule/app.xml](checkpoints/01-hello/src/main/mule/app.xml) | local-runtime-verified |
| 002 | 1 | Change the greeting / `change-greeting` | [variants/change-greeting.xml](variants/change-greeting.xml) | local-runtime-verified |
| 003 | 2 | Inspect an incoming request / `inspect-request` | [checkpoints/02-event/src/main/mule/app.xml](checkpoints/02-event/src/main/mule/app.xml) | local-runtime-verified |
| 004 | 2 | Replace the response body / `replace-response-body` | [checkpoints/02-event/src/main/mule/app.xml](checkpoints/02-event/src/main/mule/app.xml) | local-runtime-verified |
| 005 | 3 | Read an order header / `read-order-header` | [checkpoints/03-one-response/src/main/mule/app.xml](checkpoints/03-one-response/src/main/mule/app.xml) | local-runtime-verified |
| 006 | 3 | Calculate one line / `calculate-line` | [checkpoints/03-one-response/src/main/mule/app.xml](checkpoints/03-one-response/src/main/mule/app.xml) | local-runtime-verified |
| 007 | 3 | Convert a supplier price / `convert-line-price` | [checkpoints/03-one-response/src/main/mule/app.xml](checkpoints/03-one-response/src/main/mule/app.xml) | local-runtime-verified |
| 008 | 4 | Calculate every line / `calculate-lines` | [checkpoints/04-order-lines/src/main/mule/app.xml](checkpoints/04-order-lines/src/main/mule/app.xml) | local-runtime-verified |
| 009 | 4 | Calculate the order total / `order-total` | [checkpoints/04-order-lines/src/main/mule/app.xml](checkpoints/04-order-lines/src/main/mule/app.xml) | local-runtime-verified |
| 010 | 5 | Keep the order identifier / `keep-order-context` | [checkpoints/05-context-and-subflows/src/main/mule/app.xml](checkpoints/05-context-and-subflows/src/main/mule/app.xml) | local-runtime-verified |
| 011 | 5 | Extract the total calculation / `calculate-total` | [checkpoints/05-context-and-subflows/src/main/mule/app.xml](checkpoints/05-context-and-subflows/src/main/mule/app.xml) | local-runtime-verified |
| 012 | 5 | Call the calculation / `call-total` | [checkpoints/05-context-and-subflows/src/main/mule/app.xml](checkpoints/05-context-and-subflows/src/main/mule/app.xml) | local-runtime-verified |
| 013 | 5 | Change the child event / `change-child-event` | [checkpoints/05-context-and-subflows/src/main/mule/app.xml](checkpoints/05-context-and-subflows/src/main/mule/app.xml) | local-runtime-verified |
| 014 | 5 | Retain a subflow result / `targeted-subflow` | [checkpoints/05-context-and-subflows/src/main/mule/app.xml](checkpoints/05-context-and-subflows/src/main/mule/app.xml) | local-runtime-verified |
| 015 | 6 | Check the greeting and total / `first-munit-suite` | [checkpoints/06-first-tests/src/test/munit/app-test.xml](checkpoints/06-first-tests/src/test/munit/app-test.xml) | local-runtime-verified |
| 016 | 7 | Validate an order request / `validate-request` | [checkpoints/07-request-contract/src/main/mule/app.xml](checkpoints/07-request-contract/src/main/mule/app.xml) | local-runtime-verified |
| 017 | 8 | Raise an invalid-order error / `validate-order` | [checkpoints/08-error-boundaries/src/main/mule/app.xml](checkpoints/08-error-boundaries/src/main/mule/app.xml) | local-runtime-verified |
| 018 | 8 | Handle validation at the request boundary / `typed-validation` | [checkpoints/08-error-boundaries/src/main/mule/app.xml](checkpoints/08-error-boundaries/src/main/mule/app.xml) | local-runtime-verified |
| 019 | 8 | Share the public error handler / `public-errors` | [checkpoints/08-error-boundaries/src/main/mule/app.xml](checkpoints/08-error-boundaries/src/main/mule/app.xml) | local-runtime-verified |
| 020 | 8 | Recover inside a Try / `recover-optional` | [checkpoints/08-error-boundaries/src/main/mule/app.xml](checkpoints/08-error-boundaries/src/main/mule/app.xml) | local-runtime-verified |
| 021 | 9 | Load local HTTP properties / `local-http-properties` | [checkpoints/09-http-dependency/src/main/resources/config-local.yaml](checkpoints/09-http-dependency/src/main/resources/config-local.yaml) | local-runtime-verified |
| 022 | 9 | Configure the customer connection / `dependency-http-config` | [checkpoints/09-http-dependency/src/main/mule/app.xml](checkpoints/09-http-dependency/src/main/mule/app.xml) | local-runtime-verified |
| 023 | 9 | Look up the customer / `lookup-customer` | [checkpoints/09-http-dependency/src/main/mule/app.xml](checkpoints/09-http-dependency/src/main/mule/app.xml) | local-runtime-verified |
| 024 | 10 | Keep the order during enrichment / `enrich-order` | [checkpoints/10-enrichment-tests/src/main/mule/app.xml](checkpoints/10-enrichment-tests/src/main/mule/app.xml) | local-runtime-verified |
| 025 | 10 | Keep an unavailable estimate explicit / `optional-shipping` | [checkpoints/10-enrichment-tests/src/main/mule/app.xml](checkpoints/10-enrichment-tests/src/main/mule/app.xml) | local-runtime-verified |
| 026 | 10 | Mock the result the flow reads / `target-aware-munit` | [checkpoints/10-enrichment-tests/src/test/munit/app-test.xml](checkpoints/10-enrichment-tests/src/test/munit/app-test.xml) | local-runtime-verified |
| 027 | 11 | Configure the local database / `orders-database-config` | [checkpoints/11-database/src/main/mule/app.xml](checkpoints/11-database/src/main/mule/app.xml) | local-runtime-verified |
| 028 | 11 | Prepare the isolated orders table / `prepare-orders` | [checkpoints/11-database/src/main/mule/app.xml](checkpoints/11-database/src/main/mule/app.xml) | local-runtime-verified |
| 029 | 11 | Insert a calculated order / `insert-order` | [checkpoints/11-database/src/main/mule/app.xml](checkpoints/11-database/src/main/mule/app.xml) | local-runtime-verified |
| 030 | 11 | Read a stored order / `read-order` | [checkpoints/11-database/src/main/mule/app.xml](checkpoints/11-database/src/main/mule/app.xml) | local-runtime-verified |
| 031 | 12 | Roll back an inserted order / `rollback-order` | [checkpoints/12-transactions/src/main/mule/app.xml](checkpoints/12-transactions/src/main/mule/app.xml) | local-runtime-verified |
| 032 | 12 | Complete the owning Try / `continue-in-owner` | [checkpoints/12-transactions/src/main/mule/app.xml](checkpoints/12-transactions/src/main/mule/app.xml) | local-runtime-verified |
| 033 | 13 | Describe the local order API / `orders-raml` | [checkpoints/13-apikit-contract/src/main/resources/api/orders.raml](checkpoints/13-apikit-contract/src/main/resources/api/orders.raml) | local-runtime-verified |
| 034 | 13 | Map the contract to implementation flows / `orders-apikit-config` | [checkpoints/13-apikit-contract/src/main/mule/app.xml](checkpoints/13-apikit-contract/src/main/mule/app.xml) | local-runtime-verified |
| 035 | 13 | Route a request through APIkit / `orders-api` | [checkpoints/13-apikit-contract/src/main/mule/app.xml](checkpoints/13-apikit-contract/src/main/mule/app.xml) | local-runtime-verified |
| 036 | 14 | Price the accepted command / `price-order` | [checkpoints/14-local-order-api/src/main/mule/app.xml](checkpoints/14-local-order-api/src/main/mule/app.xml) | local-runtime-verified |
| 037 | 14 | Create and save the local order / `create-order` | [checkpoints/14-local-order-api/src/main/mule/app.xml](checkpoints/14-local-order-api/src/main/mule/app.xml) | local-runtime-verified |
| 038 | 14 | Retrieve the saved order / `get-order` | [checkpoints/14-local-order-api/src/main/mule/app.xml](checkpoints/14-local-order-api/src/main/mule/app.xml) | local-runtime-verified |
| 039 | 15 | Write and read an order file / `file-roundtrip` | [checkpoints/15-order-files/src/main/mule/app.xml](checkpoints/15-order-files/src/main/mule/app.xml) | local-runtime-verified |
| 040 | 15 | Normalize CSV item rows / `normalize-csv` | [checkpoints/15-order-files/src/main/mule/app.xml](checkpoints/15-order-files/src/main/mule/app.xml) | local-runtime-verified |
| 041 | 16 | Process three records sequentially / `process-records` | [checkpoints/16-sequential-and-scheduled/src/main/mule/app.xml](checkpoints/16-sequential-and-scheduled/src/main/mule/app.xml) | local-runtime-verified |
| 042 | 16 | Run the small import on a schedule / `scheduled-import` | [checkpoints/16-sequential-and-scheduled/src/main/mule/app.xml](checkpoints/16-sequential-and-scheduled/src/main/mule/app.xml) | local-runtime-verified |
| 043 | 17 | Join customer and catalogue lookups / `parallel-lookups` | [checkpoints/17-parallel-work/src/main/mule/app.xml](checkpoints/17-parallel-work/src/main/mule/app.xml) | local-runtime-verified |
| 044 | 17 | Double independent items in parallel / `parallel-items` | [checkpoints/17-parallel-work/src/main/mule/app.xml](checkpoints/17-parallel-work/src/main/mule/app.xml) | local-runtime-verified |
| 045 | 17 | Handle a failed parallel lookup / `failed-parallel-route` | [checkpoints/17-parallel-work/src/main/mule/app.xml](checkpoints/17-parallel-work/src/main/mule/app.xml) | local-runtime-verified |
| 046 | 18 | Retry a temporarily unavailable read / `retry-read` | [checkpoints/18-retry-and-idempotency/src/main/mule/app.xml](checkpoints/18-retry-and-idempotency/src/main/mule/app.xml) | local-runtime-verified |
| 047 | 18 | Accept or replay a command / `accept-once` | [checkpoints/18-retry-and-idempotency/src/main/mule/app.xml](checkpoints/18-retry-and-idempotency/src/main/mule/app.xml) | local-runtime-verified |
| 048 | 18 | Commit the order and request result / `commit-order` | [checkpoints/18-retry-and-idempotency/src/main/mule/app.xml](checkpoints/18-retry-and-idempotency/src/main/mule/app.xml) | local-runtime-verified |
| 049 | 18 | Recover the committed winner / `recover-recorded-result` | [checkpoints/18-retry-and-idempotency/src/main/mule/app.xml](checkpoints/18-retry-and-idempotency/src/main/mule/app.xml) | local-runtime-verified |
| 050 | 19 | Commit notification intent with acceptance / `commit-order-with-outbox` | [checkpoints/19-outbox/src/main/mule/app.xml](checkpoints/19-outbox/src/main/mule/app.xml) | local-runtime-verified |
| 051 | 19 | Dispatch pending order events / `dispatch-pending` | [checkpoints/19-outbox/src/main/mule/app.xml](checkpoints/19-outbox/src/main/mule/app.xml) | local-runtime-verified |
| 052 | 20 | Start a local asynchronous notice / `async-notice` | [checkpoints/20-async-and-queues/src/main/mule/app.xml](checkpoints/20-async-and-queues/src/main/mule/app.xml) | local-runtime-verified |
| 053 | 20 | Publish a local VM notice / `publish-local-notice` | [checkpoints/20-async-and-queues/src/main/mule/app.xml](checkpoints/20-async-and-queues/src/main/mule/app.xml) | local-runtime-verified |
| 054 | 20 | Consume a local VM notice / `consume-local-notice` | [checkpoints/20-async-and-queues/src/main/mule/app.xml](checkpoints/20-async-and-queues/src/main/mule/app.xml) | local-runtime-verified |
| 055 | 20 | Publish and acknowledge an MQ order event / `mq-order-delivery` | [platform/mq/src/main/mule/app.xml](platform/mq/src/main/mule/app.xml) | not-run |
| 056 | 21 | Classify a three-record Batch import / `start-batch` | [checkpoints/21-batch-import/src/main/mule/app.xml](checkpoints/21-batch-import/src/main/mule/app.xml) | local-runtime-verified |
| 057 | 21 | Record an accepted import row / `record-import-success` | [checkpoints/21-batch-import/src/main/mule/app.xml](checkpoints/21-batch-import/src/main/mule/app.xml) | local-runtime-verified |
| 058 | 21 | Record a rejected import row / `record-import-rejection` | [checkpoints/21-batch-import/src/main/mule/app.xml](checkpoints/21-batch-import/src/main/mule/app.xml) | local-runtime-verified |
| 059 | 22 | Cache a catalogue separately for each tenant / `cached-catalogue` | [checkpoints/22-cache-and-state/src/main/mule/app.xml](checkpoints/22-cache-and-state/src/main/mule/app.xml) | local-runtime-verified |
| 060 | 22 | Invalidate one tenant catalogue / `invalidate-one-tenant` | [checkpoints/22-cache-and-state/src/main/mule/app.xml](checkpoints/22-cache-and-state/src/main/mule/app.xml) | local-runtime-verified |
| 061 | 22 | Store and retrieve a local note / `store-note` | [checkpoints/22-cache-and-state/src/main/mule/app.xml](checkpoints/22-cache-and-state/src/main/mule/app.xml) | local-runtime-verified |
| 062 | 23 | Supply a local test principal / `local-test-principal` | [checkpoints/23-order-ownership/src/main/mule/app.xml](checkpoints/23-order-ownership/src/main/mule/app.xml) | local-runtime-verified |
| 063 | 23 | Require a caller tenant / `require-tenant` | [checkpoints/23-order-ownership/src/main/mule/app.xml](checkpoints/23-order-ownership/src/main/mule/app.xml) | local-runtime-verified |
| 064 | 23 | Read an order within its owner tenant / `get-owned-order` | [checkpoints/23-order-ownership/src/main/mule/app.xml](checkpoints/23-order-ownership/src/main/mule/app.xml) | local-runtime-verified |
| 065 | 23 | Trust a local TLS server / `hello-over-tls` | [platform/tls/src/main/mule/app.xml](platform/tls/src/main/mule/app.xml) | local-runtime-verified |
| 066 | 24 | Plan the orders policy boundary / `orders-policy-plan` | [platform/policies/orders-policy-plan.yaml](platform/policies/orders-policy-plan.yaml) | not-run |
| 067 | 25 | Identify a CloudHub deployment / `cloud-deployment-inputs` | [platform/cloudhub/deploy-inputs.example.properties](platform/cloudhub/deploy-inputs.example.properties) | not-run |
| 068 | 26 | Log committed acceptance or replay / `log-committed-order` | [checkpoints/26-order-investigation/src/main/mule/app.xml](checkpoints/26-order-investigation/src/main/mule/app.xml) | local-runtime-verified |
| 069 | 26 | Configure bounded local application logs / `orders-log-configuration` | [checkpoints/26-order-investigation/src/main/resources/log4j2.xml](checkpoints/26-order-investigation/src/main/resources/log4j2.xml) | not-run |
| 070 | 27 | Validate the companion in CI / `book-validation-pipeline` | [../.github/workflows/book-validation.yml](../.github/workflows/book-validation.yml) | not-run |
| 071 | 27 | Reject missing or empty test evidence / `required-munit-reports` | [check_reports.py](check_reports.py) | local-command-verified |
| 072 | 27 | Record a candidate digest / `candidate-digest` | [release_digest.py](release_digest.py) | local-command-verified |
| 073 | 28 | Design a partial order-status response / `partial-order-status` | [workshops/architecture/status-view.json](workshops/architecture/status-view.json) | design-fixture |
| 074 | 29 | Route the known orders API through Omni Gateway / `local-orders-gateway` | [platform/omni/orders.yaml](platform/omni/orders.yaml) | not-run |
| 075 | B | Retain response status with its body / `response-message-workshop` | [workshops/representations/src/main/mule/app.xml](workshops/representations/src/main/mule/app.xml) | local-runtime-verified |
| 076 | B | Normalize repeated XML items / `xml-order-adapter` | [workshops/representations/src/main/resources/normalize-xml.dwl](workshops/representations/src/main/resources/normalize-xml.dwl) | local-runtime-verified |
| 077 | B | Extract a pure pricing helper / `pricing-module` | [workshops/representations/src/main/resources/modules/Pricing.dwl](workshops/representations/src/main/resources/modules/Pricing.dwl) | local-runtime-verified |
| 078 | B | Call the imported pricing helper / `import-pricing-module` | [workshops/representations/src/main/resources/total.dwl](workshops/representations/src/main/resources/total.dwl) | local-runtime-verified |
| 079 | B | Inspect two Java numeric values / `historical-java-numbers` | [workshops/historical-formats/java-numbers.xml](workshops/historical-formats/java-numbers.xml) | historical-run-2026-09-13 |
| 080 | B | Consume deferred JSON at the listener / `historical-deferred-json` | [workshops/historical-formats/deferred-json.xml](workshops/historical-formats/deferred-json.xml) | historical-run-2026-09-13 |
| 081 | B | Round-trip a small Excel sheet / `historical-excel-roundtrip` | [workshops/historical-formats/excel-roundtrip.xml](workshops/historical-formats/excel-roundtrip.xml) | historical-run-2026-09-13 |
| 082 | B | Read a fixed-width schema / `historical-fixed-width` | [workshops/historical-formats/fixed-width.xml](workshops/historical-formats/fixed-width.xml) | historical-run-2026-09-13 |
| 083 | B | Describe order acceptance in OpenAPI / `orders-openapi-contract` | [workshops/contracts/orders.openapi.yaml](workshops/contracts/orders.openapi.yaml) | schema-reviewed-not-routed |
| 084 | C | Allocate a standalone shared listener / `standalone-shared-listener` | [workshops/domains/shared-listener.xml](workshops/domains/shared-listener.xml) | configuration-fragment-not-deployed |
| 085 | D | Select a page with a stable tiebreaker / `ordered-watermark-page` | [workshops/synchronization/page.sql](workshops/synchronization/page.sql) | query-template-not-executed |
