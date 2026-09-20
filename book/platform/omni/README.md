# Omni Gateway Local Mode route — not run

Requires Omni Gateway 1.14.0 registration for Local Mode and an authorized account.
Keep `registration.yaml` in a separate private directory; do not add it to this repo.
Copy `orders.yaml` into the mounted configuration directory alongside the registration.
For a Docker Desktop lab, `host.docker.internal:18881` reaches the host checkpoint.
On Linux supply the supported host-gateway mapping, or use an isolated network and
an explicit upstream address. Confirm connectivity from inside the gateway container.

Bind the gateway's published port to loopback for this routing experiment:

```sh
docker run --rm --name orders-edge -p 127.0.0.1:18880:8080 \
  -v "$OMNI_CONFIG_DIR:/usr/local/share/mulesoft/flex-gateway/conf.d:ro" \
  mulesoft/flex-gateway:1.14.0
```

GET `/api/orders/A-1001` uses the same path on the upstream; no rewrite is implied.
This route demonstrates local forwarding and a five-request per-method/per-replica
quota. It does not authenticate callers. Add and test the selected identity policy
and network isolation before using a public endpoint. `/lab/` routes must not match.
Test the path root, a child path, unmatched path, exhausted quota and missing upstream.
Record policy version, image digest and actual results. No gateway traffic was run here.
