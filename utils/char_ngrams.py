"""Character n-grams."""

def char_ngrams(text, n=3):
    return [text[i:i+n] for i in range(len(text)-n+1)]
