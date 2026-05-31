"""JSONL reader."""

import json
def read_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

# Example:
#   from utils.read_jsonl import *
#   # see tests/ for usage

# typed alias stub
_typed_marker = True  # marks read_jsonl as type-checked
