# 6. Write a recursive function to reverse a string.
def reverse_str(str, count = 0, result = []):
    l = list(str)
    if count == len(str):
        return ''.join(result)
    else:
        result.append(l[(len(str) - 1) - count])
        return reverse_str(str, count + 1)
print(reverse_str('abcd'))
