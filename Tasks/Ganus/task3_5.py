str_enter = input("Введите, пожалуйста, строку\n")
str_enter = str_enter.replace(',', '').replace('.', '').replace(':', '').replace('-', '').replace('!', '').replace('?', '')
str_enter = str_enter.split(" ")
new_list = []
for i in str_enter:
    i = str(i)
    if len(i) > 5:
        new_list.append(i)
    else:
        continue
print(new_list)
    
