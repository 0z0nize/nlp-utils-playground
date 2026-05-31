"""Safe division helper."""

def safe_div(a, b, default=0.0):
    return a / b if b else default

# Example:
#   from utils.safe_divide import *
#   # see tests/ for usage

# typed alias stub
_typed_marker = True  # marks safe_divide as type-checked
