l = [1,2,3,4,5,6.0,"seven",[]]
print(type(l), l, len(l))

print(l[0], l[-1], l[3:])
# l[100000] IndexError

print([1,2,3]+[4,5,6])
print([0]*10)

l[0] = 1.0
print(l)
# l[1000000] = 1000000 IndexError

l[3:4] = [4,4,4,4,4,4,4,4,4]
print(l)

l.append("new item")
print(l)

l.extend("test str")
print(l)

l.extend([8,9,10])
print(l)

l.insert(0, "new first elem")
print(l)

print('3' in l)
print(l.index(3))

l.remove(4)
print(l)

x = l.pop()
print(x, l)

x = l.pop(0)
print(x, l)

x = l.pop(0)
print(x, l)

del l[0]
del l[2:6]
print(l)

m = l
del l
# print(l) NameError
print(m)

m.clear()
print(m)

l1 = l2 = []
l2.append("test")
print(l1)