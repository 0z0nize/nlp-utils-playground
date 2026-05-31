"""Minimal TF-IDF."""

from collections import Counter
import math
def tfidf(docs):
    df = Counter()
    for d in docs:
        for t in set(d): df[t] += 1
    N = len(docs)
    return [{t: (c/len(d)) * math.log(N/df[t]) for t,c in Counter(d).items()} for d in docs]
