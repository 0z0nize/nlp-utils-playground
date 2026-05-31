"""Discounted Cumulative Gain."""

import math
def dcg(rels):
    return sum(r/math.log2(i+2) for i, r in enumerate(rels))

# Example:
#   from utils.dcg import *
#   # see tests/ for usage
