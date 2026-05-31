"""Timing context manager."""

import time
from contextlib import contextmanager
@contextmanager
def timer(label='block'):
    s = time.time(); yield; print(f'{label}: {time.time()-s:.3f}s')
