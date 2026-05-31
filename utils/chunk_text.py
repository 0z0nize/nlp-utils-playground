"""Text chunking by size."""

def chunks(text, size=512):
    return [text[i:i+size] for i in range(0, len(text), size)]
