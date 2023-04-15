# 4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols, second for count of the upper case symbols in the initial string.
def count(str):
    low = 0
    upper = 0
    for i in str:
        if i.islower():
            low += 1;
        else: 
            upper += 1
    return low, upper      
print(count('AbCDEcdscvsdfWEEEEEEEEEE'))
