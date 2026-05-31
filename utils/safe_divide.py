"""Safe division helper."""

def safe_div(a, b, default=0.0):
    return a / b if b else default
