x = [1,2,3,4,5]

# for x in x:
#     print(x)

print(id(x))
print(x)

def test_func(x):
    print(id(x))
    print(x)

def new_func():
    x = 88
    print(id(x))
    print(x)

def test_global_var():
    print(id(x))
    print(x)

def change_global():
    x.append(42)

# new_func()
# print(x)

# test_func(125)
# print(x)

change_global()
print(x)

x = 77

def change_global_value():
    global x
    x = 445
    print(x)

change_global_value()
print(x)

def outer_func():
    x = "test outer value"
    print(x)
    def inner_func():
        nonlocal x
        x = "test inner value"
        print(x)

    inner_func()
    print(x)

outer_func()
print(x)
