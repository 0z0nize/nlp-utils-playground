"""Recursive list flattener."""

def flatten(lst):
    out = []
    for x in lst:
        if isinstance(x, list): out.extend(flatten(x))
        else: out.append(x)
    return out
