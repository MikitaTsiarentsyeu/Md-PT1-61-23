# 1. Write a function that takes two numbers as input and returns their division. Handle the ZeroDivisionError and return "Cannot divide by zero"
# if the denominator is zero.

x = int(input("Enter integer value x: \n"))
y = int(input("Enter integer value y: \n"))

try:
 try:
    res = x / y
    print(res)
 except ZeroDivisionError:
    print("Cannot divide by zero")
    y = int(input("Enter integer value y: \n"))
    res = x / y
    print(res)
except:
  print("something went wrong")
