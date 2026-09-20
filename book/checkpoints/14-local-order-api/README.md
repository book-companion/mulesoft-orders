# Chapter 14: local order api

This is a complete application checkpoint for *MuleSoft from the Ground Up*.
Run commands from the companion root:

```sh
python3 book/run.py package 14
python3 book/run.py deploy 14
python3 book/run.py verify 14
```

Use an isolated Mule 4.12.3 runtime and Java 17. Set `MULE_HOME` before deployment.
Run `python3 book/stubs/server.py` separately where the chapter calls a dependency.
Only one checkpoint is deployed at a time: all use the `orders-learning` application name and loopback port 18881.
The POM retains the documented AST pre-generation workaround; successful packaging is not a runtime verification result.
See `book/README.md` for setup, cleanup and evidence scope.
