# 9. Write a program that takes a string as input and returns the string reversed.

UserText = input("Enter text:\n")
UserList = []
UserList.extend(UserText)
ReversedList = []

for i in range(len(UserList)):
    ReversedList.insert(i,UserList[-i])

ReversedList.append(ReversedList[0])
ReversedList.pop(0)

ReturnText = ''.join(ReversedList)

print(ReturnText)

