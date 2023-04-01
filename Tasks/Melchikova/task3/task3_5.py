string = list(map(str, input('Введите строку:\n').split()))

str = [s for s in string if len(s) > 5]

print(str)