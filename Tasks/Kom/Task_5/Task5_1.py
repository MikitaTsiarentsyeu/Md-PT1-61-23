#1. Write a function that takes two integers as arguments and returns their sum.

def output_sum(a:int,b:int) -> int:
    return a + b

first = int(input('enter first number:\n'))
second = int(input('enter second number:\n'))
 
print(f"The sum is:\n{output_sum(first,second)}")