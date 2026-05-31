"""Directory creator."""

import os
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# Example:
#   from utils.ensure_dir import *
#   # see tests/ for usage
