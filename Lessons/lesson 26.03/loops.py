# i = 0
# while i<10:
#     print(i)
#     i+=1

# for i in "test str":
#     print(i) 

i = 11
while True:
    if i == 0:
        break
    i-=1
    if i%2 == 0:
        continue
    print("infinity!")

count = 0
for i in "test str":
    count += 1
    if count == 5:
        break
    if i == ' ':
        # break
        continue
    print(i)

for i in [1,2,3,4,5]:
    print(i, sep=' ', end='')

print('')

for i in (1,2,3,4,5):
    print(i, sep=' ', end=' ')

print('')

for i in {1,2,3,4,5}:
    print(i, sep=' ', end=' ')

print('')

for i in '[1,2,3,4,5]':
    print(i, sep=' ', end=' ')

print('')

d = {1:"one", 2:"two"}
for i in d:
    print(i, sep=' ', end=' ')

print('')

for i in d.keys():
    print(i, sep=' ', end=' ')

print('')

for i in d.values():
    print(i, sep=' ', end=' ')

print('')

for key, value in d.items():
    print(key, value, sep=' ', end=' ')

print('')


l = [1,2,3,4,5]
for i in range(len(l)):
    print(l[i])

for i, elem in enumerate(l):
    print(i, elem)

# l = [1]
# for i in l:
#     l.append(i+1)
#     print(l)


