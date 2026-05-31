"""Recall@K."""

def r_at_k(relevant, retrieved, k):
    return len(set(retrieved[:k]) & set(relevant)) / len(relevant) if relevant else 0

# Example:
#   from utils.recall_at_k import *
#   # see tests/ for usage
