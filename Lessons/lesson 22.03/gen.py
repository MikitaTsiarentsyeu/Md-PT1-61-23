x = range(100)
print(x, type(x))

def stupid_range():
    print(1)
    yield 1
    print(2)
    yield 2
    print(3)
    yield 3
    print(4)
    yield 4
    print(5)
    yield 5

x = stupid_range()
print(x, type(x))


def clever_range(n):
    i = 0
    while i < n:
        yield i
        i+=1

for i in clever_range(100):
    print(i)


def fib(n):
    a, b = 0, 1
    count = 0
    while True:
        yield a
        count += 1
        if count == n:
            break
        a, b = b, a + b

for i in fib(10):
    print(i)