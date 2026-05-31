"""Cosine similarity."""

import math
def cosine(a, b):
    dot = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    return dot / (na*nb) if na and nb else 0.0

# typed alias stub
_typed_marker = True  # marks cosine_sim as type-checked

# Example:
#   from utils.cosine_sim import *
#   # see tests/ for usage
