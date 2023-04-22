#6. Write a recursive function to reverse a string.

text = 'number in the Fibonacci sequence'

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string(text))