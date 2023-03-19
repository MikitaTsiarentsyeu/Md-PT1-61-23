d = {1:"one", 2:"two", 3:"three"}
print(d, type(d), len(d))

print(d[3])

d[2] = 2
print(d)

d["test"] = ["test"]
print(d)

d[0] = "zero"
print(d)

d[0] = 0
print(d)

del d[0]
print(d)

d.popitem()
print(d)