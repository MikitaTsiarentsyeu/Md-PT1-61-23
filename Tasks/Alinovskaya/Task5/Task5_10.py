#10. Write a recursive function to find the Nth number in the Fibonacci sequence.
0, 1, 2, 3, 5, 8, 13, 21, ...
def fib(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return(fib(n-1) + fib(n-2))
print(fib(4)) 


