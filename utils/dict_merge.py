"""Recursive dict merge."""

def merge(a, b):
    out = dict(a)
    for k, v in b.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = merge(out[k], v)
        else: out[k] = v
    return out

# Example:
#   from utils.dict_merge import *
#   # see tests/ for usage
