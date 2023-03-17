from random import randint
num1 = int(input('Введите первое целое число: '))
num2 = int(input('Введите второе целое число: '))
if num1 > num2:
    num1, num2 = num2, num1
print(f'И это рандомное число является: {randint(num1, num2)}')
