# Chapter 12: transactions

This is a complete application checkpoint for *MuleSoft from the Ground Up*.
Run commands from the companion root:

```sh
python3 book/run.py package 12
python3 book/run.py deploy 12
python3 book/run.py verify 12
```

Use an isolated Mule 4.12.3 runtime and Java 17. Set `MULE_HOME` before deployment.
Run `python3 book/stubs/server.py` separately where the chapter calls a dependency.
Only one checkpoint is deployed at a time: all use the `orders-learning` application name and loopback port 18881.
The POM retains the documented AST pre-generation workaround; successful packaging is not a runtime verification result.
See `book/README.md` for setup, cleanup and evidence scope.
