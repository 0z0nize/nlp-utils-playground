"""Retry decorator."""

import time
def retry(n=3, delay=0.1):
    def deco(fn):
        def wrap(*a, **kw):
            for i in range(n):
                try: return fn(*a, **kw)
                except Exception:
                    if i == n-1: raise
                    time.sleep(delay)
        return wrap
    return deco

# Example:
#   from utils.retry import *
#   # see tests/ for usage
