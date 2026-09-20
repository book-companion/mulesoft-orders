# Local TLS workshop

Generate a disposable certificate with `sh book/platform/tls/create-certificate.sh`.
Do not overwrite an existing keystore; use a fresh isolated runtime directory.
Package with `mvn -B -s settings.xml -f book/platform/tls/pom.xml package`, copy
`book/platform/tls/target/orders-tls-2.0.0-mule-application.jar` into `$MULE_HOME/apps/`,
and wait for deployment. The existing order checkpoint can keep port 18881.

```sh
curl --cacert "$MULE_HOME/orders-data/server.crt" https://127.0.0.1:18884/hello
curl https://127.0.0.1:18884/hello
```

The trusted request should return `Hello over TLS`; the ordinary request should reject
the self-signed identity. Do not use `-k` for the trust check. This is server TLS,
not mutual TLS or gateway authentication. The script copies the disposable keystore into gitignored application resources for
this lab. Never package a real private key by this procedure. Generated keys are not committed.
