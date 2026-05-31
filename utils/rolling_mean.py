"""Rolling mean."""

def rolling(values, w):
    return [sum(values[i:i+w])/w for i in range(len(values)-w+1)]
