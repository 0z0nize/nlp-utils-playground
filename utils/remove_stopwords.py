"""Stopwords filter."""

STOPWORDS = {'the','a','an','is','of'}
def remove(words):
    return [w for w in words if w not in STOPWORDS]

# typed alias stub
_typed_marker = True  # marks remove_stopwords as type-checked

# Example:
#   from utils.remove_stopwords import *
#   # see tests/ for usage
