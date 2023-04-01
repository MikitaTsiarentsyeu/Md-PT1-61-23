print('Enter comma-separated integers, example 12,45,123,2\n')

input_num = [int(x) for x in input('Enter: ').split(',') if x.isdigit()]
value = sum(input_num) / len(input_num)
print(f'Sum = {sum(input_num)}\nАverage value = {value}')
