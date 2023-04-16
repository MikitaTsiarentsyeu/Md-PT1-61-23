
f = False
try:
    f = open("test1.txt", 'r')
    f.read()
except:
    print("something went wrong")
finally:
    if f:
        f.close()

# with open("test.txt", 'r') as f:
#     pass