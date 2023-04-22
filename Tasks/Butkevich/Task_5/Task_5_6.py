# 6. Write a recursive function to reverse a string.


def rever(string):
    if len(string) == 0:
        return string
    return rever(string[1:]) + string[0]


print(rever(input()))
