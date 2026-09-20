#!/usr/bin/env python3
"""Fail if required lesson MUnit reports are absent, empty or failing."""
from pathlib import Path
import xml.etree.ElementTree as ET
B = Path(__file__).resolve().parent
for folder, minimum in [('06-first-tests', 2), ('10-enrichment-tests', 1)]:
    reports = list((B / 'checkpoints' / folder / 'target/surefire-reports').glob('TEST-*.xml'))
    assert reports, f'No MUnit reports for {folder}'
    counts = dict(tests=0, failures=0, errors=0, skipped=0)
    for report in reports:
        root = ET.parse(report).getroot()
        for key in counts:
            counts[key] += int(root.get(key, '0'))
    assert counts['tests'] - counts['skipped'] >= minimum, (folder, counts)
    assert counts['failures'] == counts['errors'] == counts['skipped'] == 0, (folder, counts)
    print(folder, counts)
