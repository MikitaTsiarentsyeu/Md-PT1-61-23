print('Enter comma-separated integers, example 12,45,123,2\n')

input_num = [int(x) for x in input('Enter: ').split(',') if x.isdigit()]
value = 0

for i in input_num:
    if i % 2 == 0:
        value += i
print(f'Sum of even numbers: {value}')
