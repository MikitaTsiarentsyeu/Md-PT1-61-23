# 5. Write a decorator function that caches the return value of a function with a dictionary.
# If the function is called again with the same arguments, return the cached value instead of computing it again.


import json


def decorator(func):
    cash_new = {}

    def wrapper(*args, **kwargs):
        key = json.dumps(args) + json.dumps(kwargs)
        if key in cash_new:
            return cash_new[key]
        else:
            result = func(*args, **kwargs)
            cash_new[key] = result
            return result

    return wrapper
