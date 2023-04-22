#4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols, 
#second for count of the upper case symbols in the initial string.

d = {"upper_symbol": 0, "lower_symbol": 0}

def count_of_register (string):
    for symbol in string:
         if symbol.isupper():
            d["upper_symbol"] += 1
         else:
            d["lower_symbol"] += 1
    return d

print(count_of_register("aBcDe"))