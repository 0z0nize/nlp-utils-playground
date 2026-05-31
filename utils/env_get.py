"""Env var with default."""

import os
def env(name, default=None):
    return os.environ.get(name, default)

# Example:
#   from utils.env_get import *
#   # see tests/ for usage
