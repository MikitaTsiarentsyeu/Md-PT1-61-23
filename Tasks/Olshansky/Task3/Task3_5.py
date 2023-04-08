# Subtask 3_5
# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

users_input = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
              'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ' \
              'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum ' \
              'dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui ' \
              'officia deserunt mollit anim id est laborum.'

users_input = users_input.replace('!', '').replace('.', '').replace(',', '').replace('?', '').replace(':', '').replace(
    ';', '')
users_input = users_input.lower()
users_input = users_input.split(' ')

l =[]
for i in users_input:
    if len(i)>5:
        l.append(i)
    else:
        continue
print(l)