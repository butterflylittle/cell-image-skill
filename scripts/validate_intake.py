#!/usr/bin/env python3
import json, sys
from pathlib import Path

try:
    import jsonschema
except Exception:
    jsonschema = None

if len(sys.argv) != 2:
    print('usage: validate_intake.py <figure-intake.json>')
    raise SystemExit(2)

root = Path(__file__).resolve().parents[1]
schema = json.loads((root/'schemas/figure-intake.schema.json').read_text('utf-8'))
data = json.loads(Path(sys.argv[1]).read_text('utf-8'))

if jsonschema:
    jsonschema.validate(data, schema)
else:
    required = schema['required']
    missing = [k for k in required if k not in data]
    if missing:
        raise SystemExit('FAIL missing: ' + ', '.join(missing))

if data.get('purpose') == 'manuscript_figure' and not data.get('target_journal'):
    print('PASS (journal unspecified: use generic_high_impact and mark policy unverified)')
else:
    print('PASS')
