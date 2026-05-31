"""Basic text cleaning utility."""

def clean(text):
    return ' '.join(text.lower().split())

# Example:
#   from utils.text_clean import *
#   # see tests/ for usage
