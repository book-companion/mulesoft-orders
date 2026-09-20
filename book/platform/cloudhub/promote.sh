#!/bin/sh
set -eu
# Direct plugin goal: consume the fixed Exchange coordinates declared in pom.xml.
# Supply all -D deployment properties and a private -s settings path as arguments.
: "${MULE_CONNECTED_APP_ID:?Required platform identity}"
: "${MULE_CONNECTED_APP_SECRET:?Required platform identity secret}"
: "${ORDERS_DB_PASSWORD:?Required database secret}"
exec "${MAVEN:-mvn}" -B -f book/platform/cloudhub/pom.xml mule:deploy "$@"
