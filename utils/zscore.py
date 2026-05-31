"""Z-score normalization."""

import statistics
def zscore(values):
    m = statistics.mean(values); s = statistics.stdev(values) or 1
    return [(v-m)/s for v in values]

# Example:
#   from utils.zscore import *
#   # see tests/ for usage
