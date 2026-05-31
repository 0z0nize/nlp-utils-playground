"""JSONL writer."""

import json
def write_jsonl(path, items):
    with open(path, 'w') as f:
        for it in items: f.write(json.dumps(it, ensure_ascii=False)+'\n')

# typed alias stub
_typed_marker = True  # marks write_jsonl as type-checked

# Example:
#   from utils.write_jsonl import *
#   # see tests/ for usage
