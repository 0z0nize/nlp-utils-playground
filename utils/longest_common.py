"""Longest common substring."""

def lcs(a, b):
    best = ''
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            if a[i:j] in b and len(a[i:j]) > len(best): best = a[i:j]
    return best
