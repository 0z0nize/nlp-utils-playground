"""Mean Reciprocal Rank."""

def mrr(rankings):
    return sum(1/r if r else 0 for r in rankings) / len(rankings)
