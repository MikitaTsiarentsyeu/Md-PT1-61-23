# Напишите функцию-декоратор, которая кэширует возвращаемое значение функции со словарем. 
# Если функция вызывается снова с теми же аргументами, верните кэшированное значение, а не 
# вычисляйте его снова.
x = int(input("Enter x value\n"))
y = int(input("Enter y value\n"))

def caching(func):
    d = {}
    def wrapper(*args):
        res = func(*args)
        if args in d:
            return d[args]
        else:
            d[args] = res
            return res
    return wrapper

@caching
def sum_num(x,y):
    try:
        return int(x)+int(y)
    except ValueError:
        print("Enter only numbers")

print(sum_num(x,y))
print(sum_num(3, 18))
print(sum_num(45, 65))
print(sum_num(2, 5))
print(sum_num(3, 18))  # повтор