def exponentiation(base, degree):
    if degree == 0:
        return 1
    else:
        return base * exponentiation(base, degree - 1)
print(exponentiation(2, 5))