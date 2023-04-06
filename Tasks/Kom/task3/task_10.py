num = (input("Введите список чисел через пробел\n")).split(" ")
list = []

for i in num:
    i = int(i)
    count = 0
    if i == 2 or i % 2 != 0 and i != 1 and i != 0:
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count > 1:
            continue
        else:
            list.append(i)
list = sorted(list)
print (list[-1])