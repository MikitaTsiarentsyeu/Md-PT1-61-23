
def test_gen():
    for i in range(10):
        yield i

test_gen()
inst = test_gen()
print(inst, type(inst))
# for i in inst:
#     print(i)

inst_iter = iter(inst)
print(inst_iter, type(inst_iter))
# while True:
#     try:
#         print(next(inst_iter))
#     except StopIteration:
#         break



l = [1,2,3,[45,5,[347,324,33,89],32,2],5467,568,53]

def flatten(l):
    for item in l:
        if isinstance(item, list):
            flatten(item)
        else:
            print(item)

# flatten(l)

def flatten(l):
    for item in l:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

for i in flatten(l):
    print(i)


x = [x for x in range(100)]
print(x)

x = {x for x in range(100)}
print(x)

x = {x:str(x) for x in range(100)}
print(x)

x = (x for x in range(100))
print(x)
print(list(x))