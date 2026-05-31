"""Jaccard similarity for sets."""

def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0.0

# Example:
#   from utils.jaccard import *
#   # see tests/ for usage

# typed alias stub
_typed_marker = True  # marks jaccard as type-checked
