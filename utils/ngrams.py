"""N-gram generator."""

def ngrams(tokens, n=2):
    return list(zip(*[tokens[i:] for i in range(n)]))

# Example:
#   from utils.ngrams import *
#   # see tests/ for usage

# typed alias stub
_typed_marker = True  # marks ngrams as type-checked
