"""Basic text cleaning utility."""

def clean(text):
    return ' '.join(text.lower().split())
