# рекурсивная функция для подсчета количества вхождений данного символа в строку
a = input("Введите строку:\n")
b = input("Введите искомый элемент:\n")

def occurrences(a, b, res=0):
    if len(a) == 0:
        return res

    if a[0] == b:
        res += 1
    return occurrences(a[1:], b, res)
print(f"Элементов {b} в строке: {occurrences(a,b)}")