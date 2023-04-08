s = "word1 word2 word3 word4"
target = 40
miss = target - len(s)
count = s.count(' ')
ratio = miss//count
rem = miss%count
print(ratio)
spaces = ' '*(ratio+1)
if rem > 0:
    s = s.replace(' ', spaces)
    s = s.replace(spaces, spaces+" ", rem)
else:
    s = s.replace(' ', spaces)
print(len(s))
print(s)