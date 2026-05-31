"""Punctuation stripper."""

import string
def strip_punct(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Example:
#   from utils.strip_punct import *
#   # see tests/ for usage
