string = input('Enter the string: ')

def reverse_string(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse_string(string[:-1])
    
print(reverse_string(string))