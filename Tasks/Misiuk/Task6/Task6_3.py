def sum_even_number(*list,count=0) -> int:
    try:
        for i in list:
            if i % 2== 0:
                count += i
        return f'Sum of all even numbers in a list - {count}'
    except TypeError:
        return 'Invalid input type\nExit'


print(sum_even_number(4,3,2,6,5,8,9,3,2,6,9,0,2))
print()
print(sum_even_number(1,2,3,'sw',4,5,6,7,8,9,0,0,9,7,5,'sw'))