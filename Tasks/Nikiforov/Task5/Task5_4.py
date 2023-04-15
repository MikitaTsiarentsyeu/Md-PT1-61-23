#4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols, second for count of the upper case symbols in the initial string.

def count_cases(text:str) -> str:
    count_low = 0
    count_up = 0
    for i in text:
        if i.islower():
            count_low += 1
        elif i.isupper():
            count_up +=1 
    return f"number of lower case symbols: {count_low}\nnumber of upper case symbols: {count_up}"

print(count_cases(input('Enter some text:\n')))   