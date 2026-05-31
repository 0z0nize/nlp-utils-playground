"""Simple memoize."""

def memo(fn):
    cache = {}
    def wrap(*args):
        if args not in cache: cache[args] = fn(*args)
        return cache[args]
    return wrap
