# MuleSoft from the Ground Up — progressive companion

Begin with one greeting and add one responsibility at a time. The book has thirty
chapters and four optional appendices. This directory contains 25 complete local
Mule application checkpoints, two local workshops, and explicitly account-dependent
platform references. [Examples](EXAMPLES.md) are globally numbered in reading order;
their stable slugs, source hashes, inputs and expected results live in [examples.json](examples.json).

## First run

Use a licensed or valid evaluation Mule 4.12.3 distribution, Java 17, Maven 3.9.4
and Python 3. The repository does not distribute a runtime or a license. Dependencies
resolve through the supplied Maven settings and declared public repositories; a
first uncached build needs network access. Runtime/connector pins are in each POM.

From the repository root, set `JAVA_HOME` to your Java 17 installation and `MULE_HOME`
to a separate teaching runtime. Check `mvn -version` as well as `java -version`.
Set `MAVEN` if the intended Maven executable is not named `mvn` on PATH.

```sh
mkdir -p "$MULE_HOME/apps" "$MULE_HOME/domains/default" "$MULE_HOME/orders-data"
python3 book/run.py package 1
python3 book/run.py deploy 1
"$MULE_HOME/bin/mule" console
```

Wait for application deployment, then in another terminal:

```sh
python3 book/run.py verify 1
```

The response is `Hello, Mule!`. The book's greeting variant is a deliberate edit:
replace checkpoint 01's main XML with `book/variants/change-greeting.xml`, package
and redeploy, then inspect `Hello, Dana!`. Restore the original before using the
chapter 1 verifier, which expects the original greeting.

## Work through the checkpoints

```sh
python3 book/run.py list
python3 book/run.py package 2
python3 book/run.py deploy 2
python3 book/run.py verify 2
```

Each chapter directory is a complete project, with its own descriptor, POM, main
XML and resources. Start with the preceding checkpoint to make the lesson's edit,
or open the current checkpoint as the finished solution. Run one checkpoint at a
time: every `orders-learning` archive replaces the prior one and uses port 18881.
A deployment copy is not a readiness check; wait for the runtime's deployment result.

For chapters 9 onward, start the controlled dependencies in another terminal:

```sh
python3 book/stubs/server.py
```

They listen on 127.0.0.1:18882 and provide a customer, a catalogue, controlled failures,
call counters and a SQLite event receiver. The receiver's durable row is the entire
demonstrated downstream effect; it does not reserve inventory or take payment.
All data is synthetic. Reset and failure-injection routes belong only to this
loopback teaching application. The verification commands intentionally erase its
synthetic tables and receiver rows. Never point these projects at an existing database.

The chapter 14 checkpoint assembles the first complete local order API. Chapters
18 and 19 strengthen it with file-backed H2 request results, unique-key arbitration,
a transactional outbox and one-owner dispatch. Chapters 23, 26 and 30 keep that
service while adding explicit synthetic ownership and honest transition logging.
Earlier connector demonstrations remain in their own projects.

| Chapters | Start / finish |
| --- | --- |
| 1–6 | Greeting → event → scalar response → arrays → reuse → two MUnit tests |
| 7–14 | Validation → errors → dependency → mock → JDBC → rollback → APIkit → local API |
| 15–22 | Files → sequential/Scheduler → parallel → idempotency → outbox → queues → Batch → cache |
| 23, 26, 30 | Synthetic principal/ownership → committed logs → recovery capstone |
| 24, 25, 27–29 | Policy worksheet, CloudHub reference, CI, architecture fixture, Omni route |

`fixtures/order-calculation.json` supplies prices for arithmetic. `order-command.json`
omits prices because the API obtains them from the catalogue. A-1001 is Dana's
four pens at 2.5, two notepads at 6 and ten clips at 1: total 32 USD. Named malformed,
concurrent and restart variants keep their separate identities in the harness.

## Tests and the evidence boundary

```sh
python3 book/run.py test 6
python3 book/run.py test 10
python3 book/check_reports.py
python3 book/check_catalog.py
```

MUnit tests the actual source in those checkpoints. HTTP verification tests a separately
deployed application against real local connectors and the controlled dependency.
A package with `skipAST=true` still requires runtime deployment and behavior checks.
The AST workaround and exact coverage are explained in [verification](verification/2026-09-20.md).

The checked-in GitHub workflow runs catalogue checks, required MUnit reports and
candidate packaging/digest. It does not deploy a platform service or claim that a
unit test proves database, TLS or broker behavior. Generated `actual/`, targets,
private certificates and receiver databases are ignored.

## Workshops and platform references

- [Representations](workshops/representations/README.md): full response Message,
  XML normalization, imported module and Java object boundary; port 18887.
- [TLS](platform/tls/README.md): disposable server identity and trusted/untrusted
  requests; port 18884. Generated keystores are ignored and must remain lab-only.
- [MQ](platform/mq/README.md): complete publisher/subscriber adapter; broker access
  and acceptance tests required. Loopback publisher port 18886.
- [CloudHub](platform/cloudhub/README.md): PostgreSQL intake/outbox reference,
  deployment inputs and direct promotion script; not deployed.
- [Omni](platform/omni/README.md): Local Mode route to the known API path;
  registration and gateway traffic remain unrun.
- `workshops/historical-formats/` identifies excerpts from the unchanged root
  project. Its 13 September results are historical, not new-edition runs.

XA/domains, remote SFTP, provider token refresh, source watermarking and Connected
Mode require an environment-specific implementation/acceptance run. The book keeps
those advanced design workshops explicit rather than hiding unsupplied adapters
behind flow names. No runtime, real credential or private key is committed.
