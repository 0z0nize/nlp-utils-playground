"""Recall@K."""

def r_at_k(relevant, retrieved, k):
    return len(set(retrieved[:k]) & set(relevant)) / len(relevant) if relevant else 0
