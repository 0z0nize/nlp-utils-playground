"""Mean Reciprocal Rank."""

def mrr(rankings):
    return sum(1/r if r else 0 for r in rankings) / len(rankings)

# Example:
#   from utils.mrr import *
#   # see tests/ for usage
