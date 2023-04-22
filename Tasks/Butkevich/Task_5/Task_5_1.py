# 1. Write a function that takes two integers as arguments and returns their sum.

def summa(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b


print(summa(int(input()), int(input())))
