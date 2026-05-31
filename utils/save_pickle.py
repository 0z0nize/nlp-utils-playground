"""Pickle save helper."""

import pickle
def save(obj, path):
    with open(path, 'wb') as f: pickle.dump(obj, f)

# Example:
#   from utils.save_pickle import *
#   # see tests/ for usage
