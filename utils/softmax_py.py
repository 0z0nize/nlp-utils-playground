"""Softmax in pure Python."""

import math
def softmax(xs):
    m = max(xs); e = [math.exp(x-m) for x in xs]; s = sum(e)
    return [v/s for v in e]

# Example:
#   from utils.softmax_py import *
#   # see tests/ for usage
