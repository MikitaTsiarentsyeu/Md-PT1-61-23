import json

def cached(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = json.dumps(args) + json.dumps(kwargs)
        if key in cache:
            return cache[key]
        else:
            res = func(*args, **kwargs)
            cache[key] = res
            return res
        
    return wrapper
        