# Subtask 3_9
# 9. Write a program that takes a string as input and returns the string reversed.

users_text = 'телефон'
c = []
for i in range(len(users_text)):
    c.append(users_text[-i - 1])
print(''.join(c))
