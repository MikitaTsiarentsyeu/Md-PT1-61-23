#9. Write a recursive function to calculate the power of a given number.

def involution (n, p):
    if p == 0:
        return 0
    elif p == 1:
        return n
    else:
        return n * involution(n, p-1)

print(involution(3, 3))