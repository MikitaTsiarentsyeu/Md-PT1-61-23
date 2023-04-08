str = input("Введите список строк через пробел\n").split(" ")

list = []
for i in str:
    if len(i) > 5:
        list.append(i)
print(list)