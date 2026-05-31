"""Batching helper."""

def batches(iterable, size):
    buf = []
    for x in iterable:
        buf.append(x)
        if len(buf) == size: yield buf; buf = []
    if buf: yield buf
