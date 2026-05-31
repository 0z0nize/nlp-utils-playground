"""Argmax without numpy."""

def argmax(seq):
    return max(range(len(seq)), key=lambda i: seq[i])
