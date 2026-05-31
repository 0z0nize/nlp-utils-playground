"""Line file reader."""

def read_lines(path):
    with open(path) as f: return [l.rstrip('\n') for l in f]

# Example:
#   from utils.read_lines import *
#   # see tests/ for usage
