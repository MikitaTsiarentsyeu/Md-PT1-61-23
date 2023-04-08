num = input("Введите числа через пробел:\n").split(" ")

count = 0
for i in num:
    count += int(i)
print(f"Среднее значение {round(count / len(num),1)}")