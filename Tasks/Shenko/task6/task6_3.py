# Напишите функцию, которая принимает на вход список целых чисел и возвращает сумму всех четных чисел в списке. 
# Обработайте TypeError и верните «Недопустимый тип ввода», если ввод не является списком или не каждый элемент имеет тип int. 
l = input("Enter the numbers:\n").split()
l = list(l)


def sum_of_all_even_num(*args):
    if len(l) <= 1:
        raise TypeError
    res = 0
    for i in l:
        if int(i)%2 == 0:
            res += int(i)       
    return res
    
try:   
    print(sum_of_all_even_num(*l))
except ValueError:
        print("Enter only numbers")
except TypeError:
        print("Invalid input type")
