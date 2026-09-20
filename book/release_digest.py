#!/usr/bin/env python3
"""Record the exact candidate bytes without rebuilding them."""
import hashlib, json, subprocess, sys
from pathlib import Path
B = Path(__file__).resolve().parent
artifact = Path(sys.argv[1]).resolve()
assert artifact.is_file(), artifact
record = {'artifact': artifact.name, 'sha256': hashlib.sha256(artifact.read_bytes()).hexdigest(),
          'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=B, text=True).strip(),
          'runtime': '4.12.3', 'javaMajor': 17,
          'sourceWorktreeDirty': bool(subprocess.check_output(['git', 'status', '--porcelain'], cwd=B, text=True).strip()),
          'boundary': 'local candidate; not Exchange publication or cloud acceptance'}
(B / 'actual').mkdir(exist_ok=True)
(B / 'actual/release.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
