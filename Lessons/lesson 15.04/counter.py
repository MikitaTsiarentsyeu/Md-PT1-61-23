def counter(base):
    def inner():
        nonlocal base
        base += 1
        return base
    
    return inner

from_10 = counter(10)
print(from_10())
print(from_10())
print(from_10())

from_100 = counter(100)
print(from_100())
print(from_100())
print(from_100())
print(from_10())
print(from_10())
print(from_10())