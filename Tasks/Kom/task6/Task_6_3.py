def number(*list,count=0) -> int:
    try:
        for i in list:
            if i % 2== 0:
                count += i
        return f'Sum of all even numbers in a list - {count}'
    except TypeError:
        return 'Invalid input type\nExit'


print(number(1,3,5,7,2,4,4))
print(number(34,64,68,25,758,"rj"))