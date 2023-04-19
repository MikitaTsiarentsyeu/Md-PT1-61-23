import time
from functools import wraps
import logging


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w',
                            format='%(asctime)s %(levelname)s %(message)s')
        logging.info(f'The execution time is equal to {execution_time}')
        logging.info(f'Arguments: {args}, {kwargs}')
        logging.info(f'Return value: {return_value}')
    return wrapper


# example
@decorator
def sum_of_elements(nums):
    res = 0
    for n in nums:
        res += n
    return res


sum_of_elements([1, 2, 3, 4, 5])
