"""Batching helper."""

def batches(iterable, size):
    buf = []
    for x in iterable:
        buf.append(x)
        if len(buf) == size: yield buf; buf = []
    if buf: yield buf

# typed alias stub
_typed_marker = True  # marks batch_iter as type-checked

# Example:
#   from utils.batch_iter import *
#   # see tests/ for usage
