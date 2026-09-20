#!/bin/sh
set -eu
: "${JAVA_HOME:?Set JAVA_HOME to Java 17}"
: "${MULE_HOME:?Set MULE_HOME to the isolated teaching runtime}"
mkdir -p "$MULE_HOME/orders-data"
# Disposable demonstration password; never use this generated identity outside this lab.
"$JAVA_HOME/bin/keytool" -genkeypair -alias localhost -keyalg RSA -keysize 2048 \
  -storetype PKCS12 -keystore "$MULE_HOME/orders-data/server.p12" \
  -storepass changeit -keypass changeit -dname "CN=localhost" \
  -ext "SAN=DNS:localhost,IP:127.0.0.1" -validity 30
"$JAVA_HOME/bin/keytool" -exportcert -rfc -alias localhost \
  -keystore "$MULE_HOME/orders-data/server.p12" -storepass changeit \
  -file "$MULE_HOME/orders-data/server.crt"

# Only this disposable lab identity is packaged; the generated file is gitignored.
mkdir -p book/platform/tls/src/main/resources
cp "$MULE_HOME/orders-data/server.p12" book/platform/tls/src/main/resources/server.p12
