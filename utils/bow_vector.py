"""Bag-of-words vectorizer."""

from collections import Counter
def bow(tokens, vocab):
    c = Counter(tokens)
    return [c[v] for v in vocab]
