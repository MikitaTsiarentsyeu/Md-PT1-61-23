int_enter = input("Веведите, пожалуйста, список чисел через пробел\n")
count = 0
int_enter = int_enter.split(" ")

for i in int_enter:
    if int(i) % 2 == 0:
        count += int(i)
print(f"Сумма чётных чисел равна {count}")
