# CloudHub reference application — not deployed

This project contains the APIkit intake, PostgreSQL persistence and outbox write.
It omits local `/lab/` controls and the synthetic caller provider. Its entry flow
requires claims established by the configured Mule Gateway JWT policy; it has no
fallback caller. Only deploy behind verified policy enforcement and network controls.

Before deployment, provision a PostgreSQL database and apply `schema.sql`. Supply
`db.url`, `db.user`, `db.password`, `catalogue.host` and `api.id` as complete environment
configuration. Use a JDBC URL with the database provider's verified TLS settings.
The production catalogue must implement the sample `/catalogue` response contract
and the chosen authenticated tenant/pricing agreement. This reference uses the same
catalogue prices for all tenants; do not claim negotiated tenant pricing from it.

This is a single-intake application. Outbox dispatch is deliberately a separate
operating responsibility: deploy and test a dispatcher with a real publication target
and a declared ownership strategy before promising fulfillment. Chapter 19's one-owner
local dispatcher is executable evidence for that topology only. A CloudHub replica
count is not a distributed dispatcher lock.

The module/artifact settings are a reference, not successful deployment evidence.
PostgreSQL constraints, driver behavior, policy claims, ingress, target access and
recovery require an environment-specific acceptance run. The local H2/HTTP results
are not relabeled as PostgreSQL, CloudHub or MQ results.
