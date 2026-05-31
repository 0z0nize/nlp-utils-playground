"""Dedupe preserving order."""

def dedupe(seq):
    seen=set(); return [x for x in seq if not (x in seen or seen.add(x))]

# Example:
#   from utils.dedupe_preserve import *
#   # see tests/ for usage
