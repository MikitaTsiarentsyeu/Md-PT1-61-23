str = input("Введите несколько слов через пробел (некоторые слова можно повторять):\n").split(" ")

d = {}
for i in str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d, sep=' ', end=' \n')