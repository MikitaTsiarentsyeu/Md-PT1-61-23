int_enter = input("Веведите, пожалуйста, список чисел через пробел\n")
count = 0
int_enter = int_enter.split(" ")

for i in int_enter:
    i = float(i)
    count += i
print(f"Cреднее значение всех чисел {count/(len(int_enter))}")