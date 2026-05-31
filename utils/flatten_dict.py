"""Flatten nested dict."""

def flat(d, prefix=''):
    out = {}
    for k, v in d.items():
        nk = f'{prefix}.{k}' if prefix else k
        if isinstance(v, dict): out.update(flat(v, nk))
        else: out[nk] = v
    return out

# Example:
#   from utils.flatten_dict import *
#   # see tests/ for usage
