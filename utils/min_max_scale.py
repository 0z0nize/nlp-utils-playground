"""Min-max scaler."""

def scale(values):
    lo, hi = min(values), max(values)
    return [(v-lo)/(hi-lo) for v in values] if hi > lo else [0.0]*len(values)

# typed alias stub
_typed_marker = True  # marks min_max_scale as type-checked

# Example:
#   from utils.min_max_scale import *
#   # see tests/ for usage
