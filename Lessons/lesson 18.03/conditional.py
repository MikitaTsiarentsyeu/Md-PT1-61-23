x = 20

if x == 0:
    print("zero")
elif x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
else:
    print("idk")

x = -1

if x == 0:
    print("zero")
elif x > 0:
    print("positive")
else:
    print("negative")

x = -100
if x >= 0:
    if x == 0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")


print("True") if x else print("False")

if x:
    print("True")
else:
    print("False")

result = "True" if x > 0 else "False"

print("zero") if x == 0 else print("positive") if x>=0 else print("negative")