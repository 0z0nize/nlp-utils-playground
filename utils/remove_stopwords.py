"""Stopwords filter."""

STOPWORDS = {'the','a','an','is','of'}
def remove(words):
    return [w for w in words if w not in STOPWORDS]
