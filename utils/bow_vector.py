"""Bag-of-words vectorizer."""

from collections import Counter
def bow(tokens, vocab):
    c = Counter(tokens)
    return [c[v] for v in vocab]

# typed alias stub
_typed_marker = True  # marks bow_vector as type-checked

# Example:
#   from utils.bow_vector import *
#   # see tests/ for usage
