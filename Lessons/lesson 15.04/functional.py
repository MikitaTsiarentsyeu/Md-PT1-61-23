
from functools import reduce

def sum(x, y):
    return x+y

my_sum = lambda x, y: x+y
print(type(my_sum))
print(my_sum(2, 3))

test_str = "Abc Aac aaa bbb".split()
print(sorted(test_str, key=lambda x: x.lower()))

def transform_to_lower(x):
    return x.lower()
print(sorted(test_str, key=transform_to_lower))

print(sorted(test_str, key=str.lower))

l = list(range(1, 11))
map_res = map(print, l)
print(type(map_res))
for i in map_res: pass

print(list(map(lambda x: x**3, l)))
print(list(map(lambda x: chr(x*10), l)))

print(list(map(lambda x: chr(x*10), filter(lambda x: x%2==0, l))))
# print(list(filter(lambda x: x%2==0, l)))


print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: f'{x}-{y}', l))
print(reduce(lambda x, y: x if x > y else y, l))