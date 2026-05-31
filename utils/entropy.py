"""Shannon entropy."""

import math
from collections import Counter
def entropy(items):
    c = Counter(items); n = sum(c.values())
    return -sum((v/n)*math.log2(v/n) for v in c.values())
