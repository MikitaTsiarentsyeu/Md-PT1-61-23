l = [2,5,4,3,1,6,8,7]

target = 10
# print(l.index(target))

for i, elem in enumerate(l):
    if elem == target:
        print(f"found it! it's on the {i} index")

min_i = 0
for i, elem in enumerate(l):
    if elem < l[min_i]:
        min_i = i

print(min_i, l[min_i])
print(min(l))

sm = 0
for i in l:
    sm += i

print(sm)
print(sum(l))

test_str = "some very long str"
target = ' '
count = 0

for symbol in test_str:
    if symbol == target:
        count += 1

print(count)


def_range = set(test_str)
for symbol in def_range:
    print(f"count of {symbol} is {test_str.count(symbol)}")

d = {}
for symbol in test_str:
    if symbol in d:
        d[symbol] += 1
    else:
        d[symbol] = 1

print(d)


# l.sort()
print(sorted(l), l)


# for j in range(len(l)-1):
#     for i in range(len(l)-j-1):
#         if l[i]>l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
        
#     print(l)


for j in range(len(l)-1):
    current_i = j
    min_i = j
    for i in range(current_i, len(l)):
        if l[i] < l[min_i]:
            min_i = i

    l[current_i], l[min_i] = l[min_i], l[current_i]
    print(l)

