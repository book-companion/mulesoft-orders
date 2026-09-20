#!/usr/bin/env python3
"""Check reading order, source hashes and displayed excerpts without a Mule runtime."""
from pathlib import Path
import hashlib,json,re
B=Path(__file__).resolve().parent
rows=json.loads((B/'examples.json').read_text())
assert [r['number'] for r in rows]==list(range(1,len(rows)+1))
assert len({r['slug'] for r in rows})==len(rows)
assert [r['chapter'] for r in rows]==sorted(r['chapter'] for r in rows)
normalize=lambda s: re.sub(r'\s+','',s)
for r in rows:
    p=(B/r['source']).resolve()
    assert p.is_relative_to(B.parent),r['source']
    assert p.is_file(),r['source']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],r['slug']
    assert normalize(r['code']) in normalize(p.read_text()),r['slug']
    assert r['status'] not in ['verification-pending','variant-awaiting-run'],r['slug']
    for fixture in r['fixtures']:assert (B/fixture).is_file(),fixture
for r in json.loads((B/'checkpoints.json').read_text()):
    p=B/r['path']
    for name in ['pom.xml','mule-artifact.json','src/main/mule/app.xml']:assert (p/name).is_file(),(r,name)
print(f'{len(rows)} ordered examples: unique identities, sources, fixtures, hashes and excerpts pass')
