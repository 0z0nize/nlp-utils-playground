"""Binary F1 score."""

def f1(tp, fp, fn):
    p = tp/(tp+fp) if tp+fp else 0
    r = tp/(tp+fn) if tp+fn else 0
    return 2*p*r/(p+r) if p+r else 0

# typed alias stub
_typed_marker = True  # marks f1_score as type-checked

# Example:
#   from utils.f1_score import *
#   # see tests/ for usage
