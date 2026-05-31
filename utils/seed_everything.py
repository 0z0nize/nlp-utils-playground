"""Reproducibility seed setter."""

import random, os
def seed(s=42):
    random.seed(s); os.environ['PYTHONHASHSEED'] = str(s)
