#!/usr/bin/env python3
"""Build and deploy one explicit book checkpoint; never download a Mule runtime."""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent
REPO = BOOK.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["list", "package", "test", "deploy", "verify"])
    parser.add_argument("chapter", type=int, nargs="?")
    args = parser.parse_args()
    entries = json.loads((BOOK / "checkpoints.json").read_text())
    if args.action == "list":
        for entry in entries:
            print(f"{entry['chapter']:02d}  {entry['slug']}")
        return
    matches = [entry for entry in entries if entry["chapter"] == args.chapter]
    if len(matches) != 1:
        parser.error("Choose a checkpoint from 'python3 book/run.py list'.")
    entry = matches[0]
    project = BOOK / entry["path"]
    if args.action in ("package", "test"):
        if args.action == "test" and not entry["tests"]:
            parser.error("This checkpoint has no MUnit suite; use its HTTP verification instead.")
        command = [os.environ.get("MAVEN", "mvn"), "-B", "-s", str(REPO / "settings.xml"), "-f", str(project / "pom.xml"), args.action]
        subprocess.run(command, check=True)
    elif args.action == "deploy":
        runtime = os.environ.get("MULE_HOME")
        if not runtime:
            parser.error("Set MULE_HOME to your isolated licensed/evaluation runtime.")
        runtime = Path(runtime).resolve()
        if not (runtime / "bin" / "mule").is_file():
            parser.error("MULE_HOME does not contain bin/mule.")
        artifact = project / "target" / "orders-learning-2.0.0-mule-application.jar"
        if not artifact.is_file():
            parser.error("Package this checkpoint first.")
        (runtime / "apps").mkdir(exist_ok=True)
        (runtime / "orders-data").mkdir(exist_ok=True)
        shutil.copy2(artifact, runtime / "apps" / artifact.name)
        print("Copied orders-learning. Wait for DEPLOYED in the runtime log before sending requests.")
    else:
        subprocess.run([sys.executable, str(BOOK / "verify.py"), str(args.chapter)], check=True)


if __name__ == "__main__":
    main()
