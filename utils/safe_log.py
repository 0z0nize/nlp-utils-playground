"""Safe log with epsilon."""

import math
def safe_log(x, eps=1e-9):
    return math.log(max(x, eps))

# Example:
#   from utils.safe_log import *
#   # see tests/ for usage
