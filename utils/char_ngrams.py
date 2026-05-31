"""Character n-grams."""

def char_ngrams(text, n=3):
    return [text[i:i+n] for i in range(len(text)-n+1)]

# typed alias stub
_typed_marker = True  # marks char_ngrams as type-checked

# Example:
#   from utils.char_ngrams import *
#   # see tests/ for usage
