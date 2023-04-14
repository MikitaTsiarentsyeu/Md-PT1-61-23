'''написать функцию, кот. принимает упорядоченный список чисел без дубликатов
               и возвращает строку с диапазонами этих чисел'''

num = input("Введите числа через пробел:\n")
num = set(int(i) for i in num.split())        #избавляемся от дубликатов
l = list(num)                                 #например [1 2 3 5 7 8 9]

def get_ranges(num):
    res = str(l[0])                      
    for i in range(len(l)-1):
        if l[i] + 1 == l[i+1]:
            if res[-1] != "-":
                res += "-"
            else:
                continue
        elif f"{l[i]}" not in res:   
            res += f"{l[i]}, {l[i+1]}"
        else:
            res += f", {l[i+1]}"
    if res[-1] == "-":
        res += f"{l[i+1]}"
    return res
print(get_ranges(num))