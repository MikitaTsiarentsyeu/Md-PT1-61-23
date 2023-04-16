import time

def do_twice(func):
    def wrapper(val1, val2):
        res1=func(val1, val2)
        res2=func(val1, val2)
        return res1, res2
    return wrapper

def info(func):
    def wrapper(a, b):
        print("The function execution is started")
        res = func(a, b)
        print("The function execution is ended")
        return res
    return wrapper

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        res = func(*args, **kwargs)
        end = time.time()
        print(f"The execution time is {end - start}")
        return res
    return wrapper

@do_twice
def test_func():
    print("test test test")

@do_twice
def test_sum(x, y):
    return x+y

@timeit
@info
def test_mult_return(x, y):
    return x*10, y*10

# test_mult_return = timeit(test_mult_return)
# test_mult_return = info(test_mult_return)

print(test_mult_return(2, 3))

# print(test_sum(2,3))

# test_func = do_twice(test_func)


# test_func()


# test_func()



# test_func()