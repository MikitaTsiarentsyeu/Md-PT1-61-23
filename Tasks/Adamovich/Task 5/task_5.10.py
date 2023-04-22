#10. Write a recursive function to find the Nth number in the Fibonacci sequence.
#0, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))