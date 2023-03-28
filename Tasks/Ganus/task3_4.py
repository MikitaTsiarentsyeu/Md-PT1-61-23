
str_list = input("Введите, пожалуйста, список чисел через пробел\n")
str_list = str_list.split(" ")
new_list = sorted(str_list)
number_count = -1
for i in range(len(new_list)):
    if new_list[number_count] != new_list[(number_count) - (i)]:
        print(new_list[(number_count) - (i)])
        break
   




