#6. Write a program that takes a string as input and returns the string with all vowels removed.
UserStrings = input("Enter text:\n")
Vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]

UserList = []
UserList.extend(UserStrings)

for i in Vowels:
    while i in UserList:
        UserList.remove(i)

for i in range(len(UserList)):
    print(UserList[i], end = "")



