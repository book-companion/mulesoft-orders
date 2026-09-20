# Representation workshop

Package the complete project with Java 17 and Maven 3.9.4:

```sh
mvn -B -s settings.xml -f book/workshops/representations/pom.xml package
cp book/workshops/representations/target/orders-representations-2.0.0-mule-application.jar "$MULE_HOME/apps/"
```

Start the dependency service on 18882. The workshop listens on 18887 and can coexist
with a checkpoint. POST the calculation fixture to `/message` and `/module`; POST
`book/fixtures/order.xml` to `/xml` with `Content-Type: application/xml`; GET `/java`.
The examples show a full target Message, XML normalization, a pure imported helper
and an actual Java Map boundary. They do not test arbitrary POJO/bean interop.
