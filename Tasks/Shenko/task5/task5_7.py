#Написать рекурсивную функцию для проверки  того, является ли заданная строка палиндромом

s = input("Введите слово, или словосочетание палиндром (напр. шалаш):\n")
s = s.replace(" ", "").replace(".", "").replace(",", "").replace("-", "").lower()    

def palindrom(s):
    if len(s) < 1:
        return True
    elif s[0] == s[-1]:
        return palindrom(s[1:-1])
    else:
        return False
    
if palindrom(s) == True:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")


    
