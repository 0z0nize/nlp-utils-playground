"""Value clipping."""

def clip(v, lo, hi):
    return max(lo, min(hi, v))

# Example:
#   from utils.clip import *
#   # see tests/ for usage
