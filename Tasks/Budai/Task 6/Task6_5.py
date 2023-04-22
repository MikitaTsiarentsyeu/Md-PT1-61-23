from functools import wraps


cache = {}


def cache_decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key_parts = func.__name__
        for arg in args:
            key_parts += str(arg)
        key = '-'.join(key_parts)
        print(key)
        res = cache.get(key)
        if res is None:
            value = func(*args, **kwargs)
            cache[key] = value
        else:
            value = cache.get(key)
        return value
    return wrapper
