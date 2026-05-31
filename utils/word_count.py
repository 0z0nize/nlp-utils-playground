"""Word frequency counter."""

from collections import Counter
def wc(text):
    return Counter(text.lower().split())
