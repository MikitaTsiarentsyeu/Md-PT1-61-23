# 10. Write a recursive function to find the Nth number in the Fibonacci sequence.
# 0, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(int(input())))
