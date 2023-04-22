# 4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols,
# second for count of the upper case symbols in the initial string.


def count_registr(a: str) -> str:
    d = {"lower": 0,
         "upper": 0
         }
    for i in a:
        if i == i.lower():
            d["lower"] += 1
        elif i == i.upper():
            d["upper"] += 1

    return d


print(count_registr(input()))
