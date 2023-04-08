
def add(a, b):
    res = a+b
    return res

add(2, 3)

def level1():
    print("this is level 1")
    level2()

def level2():
    print("this is level 2")

level1()

print(type(level1))

def test_args(x, y):
    print(f"x value is {x}")
    print(f"y value is {y}")

test_args(1, 2)
test_args(2, 1)
# test_args(1,1,1,1,1,1) error

def test_int(x):
    x+=2
    return x

target = 5
test_int(target)
print(target)

def test_list(x):
    print(id(x))
    x[0]+=2
    print(id(x))
    return x


target = [5]
print(id(target))
test_list(target)
print(id(target))
print(target)

def test_return_value(x):
    print("the function started")
    return x
    print("the function finished")

test_return_value(1)

def is_even(x):
    if x % 2 == 0:
        return True
    return False

def is_even(x):
    return x % 2 == 0
    
is_even(2)

def without_return():
    print("I'm useless")
    return

res = without_return()
print(res)

def return_something(x, y):
    return x, y

val1, val2 = return_something(1, 2)
print(val1, val2)