# 10. Write a recursive function to find the Nth number in the Fibonacci sequence.
# 0, 1, 2, 3, 5, 8, 13, 21, ...

nth = 21

def fibon(numb):
    while numb > 1:
        return fibon(numb-1) + fibon(numb-2)
    else:
        return numb

print(fibon(nth))