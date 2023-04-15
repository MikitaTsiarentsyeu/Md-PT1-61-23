# функция которая вернет список со всеми строками, длина которых превышает 5 символов

str = input("Введите список строк через пробел\n").split(" ")

def len_list5(str):
    return [x for x in str if len(x) > 5]

print(len_list5(str))