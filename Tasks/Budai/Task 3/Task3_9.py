string = input('Input string: ')

# reversed_string = string[::-1]

chars = list(string)

for i in range(len(string) // 2):
    temp = chars[i]
    chars[i] = chars[len(string) - i - 1]
    chars[len(string) - i - 1] = temp

reversed_string = ''.join(chars)

print(f'Reversed string - {reversed_string}')
