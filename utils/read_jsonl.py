"""JSONL reader."""

import json
def read_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]
