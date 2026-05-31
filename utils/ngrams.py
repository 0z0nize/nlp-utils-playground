"""N-gram generator."""

def ngrams(tokens, n=2):
    return list(zip(*[tokens[i:] for i in range(n)]))
