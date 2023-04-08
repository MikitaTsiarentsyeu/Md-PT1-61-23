l = [1,2,3,4,5,6,7,8,9,10]

print([x*x for x in l], l)

new_l = [x*x for x in l]

# new_l = []
# for x in l:
#     new_l.append(x*x)

print([x for x in range(100) if x%3==0 or x%2==0])

# new_l = []
# for x in l:
#     if x%3==0 and x%2==0:
#         # if x%2==0:
#         new_l.append(x*x)

print([x*y for x in range(1, 3) for y in range(1, 3)])
for x in range(1, 3):
    for y in range(1, 3):
        x*y

print([s for s in "s"])

print({x for x in range(1,6)})
print({x:str(x) for x in range(1,6)})

sq = (x*x for x in range(1000000))
# for i in sq:
#     print(i)

print(list(sq))