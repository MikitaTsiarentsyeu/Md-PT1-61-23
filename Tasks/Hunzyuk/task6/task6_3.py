number_list = [1, 4, 6, 3, 65, 22, 11]

def sum_elem_list(number_list):
    count = 0
    try:
        if type(number_list) !=  list:
            raise TypeError(f'Invalid input type')
        for i in number_list:
            if type(i) != int:
                raise TypeError(f'Invalid input type')
            if i % 2 == 0:
                count += i
        return count
    except Exception as ex:
        return ex
        
    
print(sum_elem_list(number_list))
    
