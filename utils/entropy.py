"""Shannon entropy."""

import math
from collections import Counter
def entropy(items):
    c = Counter(items); n = sum(c.values())
    return -sum((v/n)*math.log2(v/n) for v in c.values())

# Example:
#   from utils.entropy import *
#   # see tests/ for usage

# typed alias stub
_typed_marker = True  # marks entropy as type-checked
