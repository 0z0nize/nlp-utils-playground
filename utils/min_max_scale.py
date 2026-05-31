"""Min-max scaler."""

def scale(values):
    lo, hi = min(values), max(values)
    return [(v-lo)/(hi-lo) for v in values] if hi > lo else [0.0]*len(values)
