# Account-dependent MQ adapter — not run

Requires a licensed Anypoint MQ environment, a queue and MQ client credentials, plus
access to the connector artifact in the selected Maven repository. Supply `mq.url`,
`mq.queue`, `mq.clientId`, `mq.clientSecret`, `receiver.host`, and `receiver.port`
through protected runtime properties. Never put real values in source control.

Start the controlled receiver (`python3 book/stubs/server.py`) on the same machine for
a standalone lab. Configure `receiver.host=127.0.0.1` and `receiver.port=18882` only in
that topology. The adapter accepts event JSON on loopback port 18886 and publishes it
to the real queue. The subscriber sends the event to the receiver and ACKs afterward.

For the chapter 19 dispatcher, use this adapter's port 18886 as the publication target.
The subscriber's receiver remains on 18882; do not point it back at the publisher.
Record a valid delivery, duplicate event, receiver failure, ACK failure and redelivery.
No local VM or HTTP test establishes MQ behavior. Deployment and broker tests for
this adapter have not been performed in this edition.
