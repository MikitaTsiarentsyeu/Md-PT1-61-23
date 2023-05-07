# Write a decorator function that logs the execution time, arguments and return value of a function to a file.

import time

def logger(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = function(*args, **kwargs)
        end = time.time()
        with open("log_file_for_task_6.4.txt", "w") as file:
          file.write(f'The execution time - {start - end}, arguments - {args}, {kwargs}, return value of a function - {res}')
        return res
    return wrapper

@logger
def sum_of_two_numbers(x, y):
    return x + y

x = 1
y = 3

print(sum_of_two_numbers(x, y))
