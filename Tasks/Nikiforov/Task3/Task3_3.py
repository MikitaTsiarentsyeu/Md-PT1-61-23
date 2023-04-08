#3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
UserText = input("Enter text:\n")
UserList = UserText.split(" ")
d = {}

UserSet = set(UserList)

for word in UserSet:
    count = UserList.count(word)
    d[word] = count

print(d)




