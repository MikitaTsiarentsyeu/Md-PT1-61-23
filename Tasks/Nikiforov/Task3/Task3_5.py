# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
UserStrings = input("Enter text:\n")
UserList = UserStrings.split(" ")
ReturnList = []

for i in range(len(UserList)):
    if len(UserList[i]) > 5:
        ReturnList.append(UserList[i])

print(ReturnList)
