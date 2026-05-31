"""Sliding window iterator."""

def sliding(seq, n):
    return [seq[i:i+n] for i in range(len(seq)-n+1)]
