# 4. Write a decorator function that logs the execution time, arguments and return value of a function to a file.
import time

def log(my_file):
    def decotrator(func):
        def wrapper(args):
            with open(my_file, 'w') as f:
                start = time.time()
                f.write(f"Arguments: {args}\n")
                return_value = func(args)
                end = time.time()
                f.write(f"Return value: {return_value}\nExcution time: {end - start} sec\n")
                return return_value
        return wrapper
    return decotrator
    
@log('Tasks/Nikiforov/Task6/new_file.txt')
def cars(name):
    car = input("What is you favorite car model?\n")
    return f"{name}, your favorite car model is {car}"

cars('Andrew')






