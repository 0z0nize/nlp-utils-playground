"""Value clipping."""

def clip(v, lo, hi):
    return max(lo, min(hi, v))
