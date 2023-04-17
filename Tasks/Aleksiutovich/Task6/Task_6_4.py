# -*- coding: utf-8 -*-
import time
import logging
from functools import wraps
# Write a decorator function that logs the execution time,
# arguments and return value of a function to a file.

def log_to_file(file_name):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            with open(file_name, 'a') as f:
                f.write(f"Function: {func.__name__}\n")
                f.write(f"Arguments: {args} {kwargs}\n")
                f.write(f"Return Value: {result}\n")
                f.write(f"Execution Time: {execution_time:.6f} seconds\n\n")
            return result
        return wrapper
    return log_decorator

def logs_execution_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        this_process = func(*args, **kwargs)
        end = time.time()
        time_work = start - end
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.info(f"The execution time is equal to {time_work}")
        return this_process

    return inner


def logs_arguments(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        saved_args = locals()
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.info("The execution arguments : " + str(saved_args))
        x = func(*args, **kwargs)
        return x
    return new_func


def write_to_file(func):
    @wraps(func)
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        with open('test.txt', 'w') as f:
            f.write(x)
        return x
    return inner




# @logs_execution_time
# @logs_arguments
# @write_to_file
@log_to_file('test1.txt')
def function1(a, b):
    c = a + b
    return f"This is the first function. A + B = {c}"


@logs_execution_time
@logs_arguments
@write_to_file
def function2(c):
    return "This is the second function."


@logs_execution_time
@logs_arguments
@write_to_file
def function3(a, b, c, d):
    return "This is the third function."


# test
print(function1(5, 6))
print(function2("This is string"))
print(function3(78, 545, [x for x in range(10)], {'y': 3, 'n': 6}))
