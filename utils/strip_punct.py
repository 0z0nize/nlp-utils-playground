"""Punctuation stripper."""

import string
def strip_punct(text):
    return text.translate(str.maketrans('', '', string.punctuation))
