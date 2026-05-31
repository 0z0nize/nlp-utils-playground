"""JSONL writer."""

import json
def write_jsonl(path, items):
    with open(path, 'w') as f:
        for it in items: f.write(json.dumps(it, ensure_ascii=False)+'\n')
