# 10. Write a recursive function to find the Nth number in the Fibonacci sequence.
# 0, 1, 2, 3, 5, 8, 13, 21, ...

nth = 9

def fib(numb):
    while numb > 1:
        return fib(numb-1) + fib(numb-2)
    else:
        return numb

print(fib(nth))

    