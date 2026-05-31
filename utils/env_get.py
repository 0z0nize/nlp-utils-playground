"""Env var with default."""

import os
def env(name, default=None):
    return os.environ.get(name, default)
