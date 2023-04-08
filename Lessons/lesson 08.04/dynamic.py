
def times(a:object, b:object):
    return a*b

print(times(2, 3))
print(times(2, 3.0))
print(times([2], 3))
print(times('2', 3))
# print(times(print, 3)) error

def times_for_int(a:int, b:int) -> int:
    """
    this function will multiply int values only
    params:
    a - int value to multiply
    b - int value to multiply
    returns the multipliccation of a nd b - a*b
    """
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times_for_int("2", 4))

print(isinstance(2, object))
print(isinstance('2', object))
print(isinstance([2], object))
print(isinstance(print, object))

print([1,2,3,3,3] == [3,2,1])

def eq(l1, l2):
    if l1 is l2:
        return True
    return set(l1) == set(l2)

def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq([1,2,3], [3,3,3,2,1]))
print(eq((1,2,3), [3,3,3,2,1]))
print(eq({1,2,3}, [3,3,3,2,1]))
print(eq("123", ['3','3','3','2','1']))