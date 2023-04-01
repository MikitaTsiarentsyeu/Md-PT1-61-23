enter = input("Введите, пожалуйста, список чисел через пробел\n")
enter = enter.split(" ")
new_list = []

for i in enter:
    count = 0
    i = int(i)
    if (i == 2) or (i % 2 != 0) and (i != 1) and ( i != 0):
        for j in range(1, i):
            if i % j == 0:
                count += 1
               
        if count > 1:
            continue
        else:
            new_list.append(i)
                
                
print(max(new_list))

    
