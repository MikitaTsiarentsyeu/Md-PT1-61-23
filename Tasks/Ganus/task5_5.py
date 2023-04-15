def ranges_numbers(a: list):

    new_list = []
    new_str = ""
    for i in range(len(a)-1):
        if a[i+1] - a[i] == 1:
            new_list.append(a[i])
        else:
            new_list.append(a[i])
            if len(new_list) == 1:
                new_str = new_str + str(new_list[0]) + ","
                new_list = []
           
            else:
                new_str = new_str + str(new_list[0]) + "-" + str(new_list[-1]) + ","
                new_list = []
    for i in a[-2:]:
         if a[-2] - a[-1] == 1:
             new_list.append(a[-1])
             if len(new_list) == 1:
                 new_str = new_str + str(new_list[0])
                 break
             else:
                 new_str = new_str + str(new_list[0]) + "-" + str(new_list[-1])
                 break
         else:
             if len(new_list) != 0:
                 new_list.append(a[-1])
                 new_str = new_str + str(new_list[0]) + "-" + str(new_list[-1])
                 break
             else:
                 new_list = []
                 new_list.append(a[-1])
                 new_str = new_str + str(new_list[0])
                 break
    
    
        
    return new_str
a = [0, 1, 2, 3, 4, 7, 8, 10]
print(ranges_numbers(a))
a = [4, 7, 10]
print(ranges_numbers(a))
a = [2, 3, 8, 9]
print(ranges_numbers(a))




