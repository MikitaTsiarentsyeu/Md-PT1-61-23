def evaluate(value1, value2, value3):
    return value1+value2*value3

print(evaluate(1,value3=2,value2=3))

def choose_pet_name(name="Zephyrka"):
    print(f"Your pet is called {name} now")

choose_pet_name("Toto")
choose_pet_name()

def evaluate(value1, value2=2, value3=3):
    return value1+value2*value3

print(evaluate(3))

# print(2,3,4,5,6,7,8,9)

def sum(*values):
    print(values)
    res = 0
    for i in values:
        res+=i
    return i

sum(1,2,3,4,5,6,7,8,9,10)
l = [11,12,13,14,15]
sum(*l)

def my_print(x, y, *args, sep='-', end='.\n',):
    print(*args, sep=sep, end=end)

my_print(*[1,2,3,4,5],*[6,7,8,9],sep=' ',end='\n')

def calling_pets(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k} the {v}")

calling_pets(kitty="cat", mark="dog", donald="duck")
# calling_pets(**{1:"cat", 2:"dog"}) error

def everything(x, y, *args, test="test", **kwargs):
    print(x, y)
    print(args)
    print(test)
    print(kwargs)

everything(1,2,3,4,5,test="new value",end='.',sep=' ')
