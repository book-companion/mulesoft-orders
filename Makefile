package:
	mvn -B -s settings.xml package
verify:
	python3 verify.py
test:
	mvn -B -s settings.xml -f munit/pom.xml test
