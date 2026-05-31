"""Precision@K."""

def p_at_k(relevant, retrieved, k):
    return len(set(retrieved[:k]) & set(relevant)) / k
