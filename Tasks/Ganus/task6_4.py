import timeit
def decor(func):
    def new_function(*args, **kwargs):
        execution_time = timeit.timeit()
        result = func(*args, **kwargs)
        print(f"Время выполнеия - {execution_time}, аргумены - {args}, {kwargs}, возвращаемое значение - {result}")
    return new_function

@decor
def new_sum(a, b):
    try:
        return a + b
    except TypeError:
        print("Invalid input type")


a = 5
b = 4
new_sum(a, b)
