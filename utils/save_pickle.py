"""Pickle save helper."""

import pickle
def save(obj, path):
    with open(path, 'wb') as f: pickle.dump(obj, f)
