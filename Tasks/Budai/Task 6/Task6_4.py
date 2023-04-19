import time
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        with open('test1.txt', 'w') as file:
            file.write(f'execution time: {execution_time}\n')
            file.write(f'arguments: {args}, {kwargs}\n')
            file.write(f'return value: {return_value}\n')
    return wrapper


# example
@decorator
def sum_of_elements(nums):
    res = 0
    for n in nums:
        res += n
    return res


sum_of_elements([1, 2, 3, 4, 5])
