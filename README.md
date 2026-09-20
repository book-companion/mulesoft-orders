# MuleSoft orders companion

## Progressive edition

Start with [the book checkpoints](book/README.md) for the rewritten edition: a greeting, small transformations and tests, a complete local API, then recovery and platform workshops. The [example catalogue](book/EXAMPLES.md) follows the book's numbered reading order. New and historical results are separated in the [verification record](book/verification/2026-09-20.md).

## Historical baseline — 13 September 2026

Companion code for *MuleSoft from the Ground Up* by Simon Sarkar. It is the local Mule application the book's local checks ran against: a small order lab with database, file, routing and DataWeave format examples, a Python harness that asserts fifteen responses, and a separate MUnit project with four tests. The follow-on book, *DataWeave in Depth*, has its own [companion](https://github.com/book-companion/dataweave-orders).

## Requirements

A licensed or evaluation Mule 4.12.3 runtime, Java 17, Maven and Python 3. No Mule runtime distribution, credentials or cloud deployment is included.

Pins: Mule 4.12.3 with DataWeave 2.12.3, Mule Maven Plugin 4.10.0, HTTP Connector 1.11.3, Database Connector 1.15.1, File Connector 1.5.5 and H2 2.3.232.

## Run it

```bash
make package                                    # builds target/integration-order-lab-1.0.0-mule-application.jar
mkdir -p "$MULE_HOME/orders-data"               # the File connector's working directory
cp target/integration-order-lab-1.0.0-mule-application.jar "$MULE_HOME/apps/"
"$MULE_HOME/bin/mule" console                   # start the runtime, in a separate terminal
make verify                                     # once deployed: fifteen asserted responses, written to results/
make test                                       # the MUnit 3.7.4 project under munit/
```

The harness talks only to `127.0.0.1:18081`. The MUnit project listens on `127.0.0.1:18082`, so the two can run at the same time. Its shipping-operation mock lives in that separate project, so a mock-only configuration cannot be deployed by accident. The recorded MUnit result is 4 tests, 0 errors, 0 failures and 0 skipped on the embedded Mule 4.12.3 engine. Surefire reports are not included, because they carry machine-specific metadata.

## Before you run it

This is a teaching lab, not a production order API. `/orders` calculates a summary. `/lab/db/setup` creates the in-memory H2 table and deletes all of its rows, so the checks repeat. The other `/lab/` paths are diagnostics for database insert, select and rollback, file serialization, deferred output, Flow Reference targets, router results, and the Java, Excel and fixed-width formats. None of them is authenticated. Keep the listener on loopback, use an isolated runtime, and never point the configuration at an existing database. The file check overwrites `orders-data/order.json`, and the H2 data disappears when the process stops.

The POM sets `skipAST=true`, because the public Maven repository could not resolve the 4.12.3 runtime BOM that AST pre-generation needs. A successful package is therefore not full validation. The runtime still has to parse and deploy the archive, and the harness has to pass. During development the runtime rejected an invalid empty database password attribute that packaging had allowed.

`results/` holds the records from the local run on 13 September 2026. CloudHub, Runtime Fabric, Anypoint MQ, remote SFTP, API Manager policies, Monitoring, Omni Gateway, custom POJOs, XA and domains, production idempotency and outbox, and broader MUnit failure scenarios were not run. The book's capstone lists acceptance scenarios for them.
