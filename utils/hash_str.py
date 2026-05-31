"""Stable string hash."""

import hashlib
def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]
