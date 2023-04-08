num = input("Введите числа через пробел\n").split(" ")

list = []
for i in num:
    i = int(i)
    list.append(i)
    list.sort()

print(f"Второе по величине число в списке: {list[-2]}")