# 5. Write a decorator function that caches the return value of a function with a dictionary. 
# If the function is called again with the same arguments, return the cached value instead of computing it again.

def cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            return res
    return wrapper

@cache
def greetings(name):
    return f'Hello, {name}'

print(greetings('Andrey'))