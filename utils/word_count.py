"""Word frequency counter."""

from collections import Counter
def wc(text):
    return Counter(text.lower().split())

# Example:
#   from utils.word_count import *
#   # see tests/ for usage
