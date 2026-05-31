"""Levenshtein distance."""

def lev(a, b):
    if len(a) < len(b): a, b = b, a
    prev = list(range(len(b)+1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1]+1, prev[j]+1, prev[j-1]+(ca!=cb)))
        prev = cur
    return prev[-1]

# typed alias stub
_typed_marker = True  # marks levenshtein as type-checked

# Example:
#   from utils.levenshtein import *
#   # see tests/ for usage
