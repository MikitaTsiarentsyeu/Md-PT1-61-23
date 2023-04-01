# посчитать сумму всех четных чисел

num1 = input("Введите число 1:\n")
num2 = input("Введите число 2:\n")
num3 = input("Введите число 3:\n")     
num4 = input("Введите число 4:\n")
num5 = input("Введите число 5:\n")

list = [num1, num2, num3, num4, num5]
sum = 0
for i in list:
    if i.isdigit():
        if int(i)%2 == 0:
            sum += int(i)
print(f"Сумма всех четных чисел в строке равна {sum}.")

#или 
# numbers = input("Ведите числа через пробел:")
# num = numbers.split(" ")
# sum = 0
# for i in num:
#     if int(i)%2 == 0:
#         sum += int(i)
# print(f"Сумма всех четных чисел в строке равна {sum}.")