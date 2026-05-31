"""Unicode normalization."""

import unicodedata
def nfkc(text):
    return unicodedata.normalize('NFKC', text)

# Example:
#   from utils.normalize_unicode import *
#   # see tests/ for usage
