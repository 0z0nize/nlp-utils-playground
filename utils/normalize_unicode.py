"""Unicode normalization."""

import unicodedata
def nfkc(text):
    return unicodedata.normalize('NFKC', text)
