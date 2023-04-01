# 7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.

#normal people method:
UserStrings = input("Enter text:\n")
print(UserStrings.swapcase())


#smokers method:
UserStrings = input("Enter text once again:\n")
UserList = []
UserList.extend(UserStrings)

for i in range(len(UserList)):
    if UserList[i].islower() == True:
        UserList[i] = UserList[i].upper()
    else:
        UserList[i] = UserList[i].lower()    
    print(UserList[i], end = "")




