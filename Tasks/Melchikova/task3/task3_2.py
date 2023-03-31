x = input("Введите список чисел\n")
count = 0

for i in x:
    if int(i) % 2 == 0:
        count += int(i)
print('Сумма четных чисел равна', count)