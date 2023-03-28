str_enter = input("Введите, пожалуйста, строку\n")
str_enter = str_enter.lower()
str_enter = str_enter.replace("у","").replace("е","").replace("ы","").replace("а","").replace("о","").replace("э","").replace("я","").replace("и","").replace("ю","").replace("ё","")
print(str_enter)
