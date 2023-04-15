# 8. Write a recursive function to count the number of occurrences of a given character in a string.

def count_symbol(string, letter):
    if len(string) == 0:
        return 0
    else:
        if string[0] == letter:
            return 1 + count_symbol(string[1:], letter)
        else:
            return count_symbol(string[1:], letter)


print(count_symbol(input(), input()))
