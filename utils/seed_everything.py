"""Reproducibility seed setter."""

import random, os
def seed(s=42):
    random.seed(s); os.environ['PYTHONHASHSEED'] = str(s)

# typed alias stub
_typed_marker = True  # marks seed_everything as type-checked

# Example:
#   from utils.seed_everything import *
#   # see tests/ for usage
