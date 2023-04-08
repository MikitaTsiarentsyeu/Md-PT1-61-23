# Subtask 3_3
# 3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.

users_input = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
              'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ' \
              'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum ' \
              'dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui ' \
              'officia deserunt mollit anim id est laborum.'

users_input = users_input.replace('!', '').replace('.', '').replace(',', '').replace('?', '').replace(':', '').replace(
    ';', '')
users_input = users_input.lower()
users_input = users_input.split(' ')
# print(users_input)

d = {}
for words in users_input:
    if words in d:
        d[words] += 1
    else:
        d[words] = 1
print(d)
