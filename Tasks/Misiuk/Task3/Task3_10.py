print('Enter comma-separated integers, example 12,45,123,2\n')
input_num = [int(x) for x in input('Enter: ').split(',') if x.isdigit()]

list_output = sorted(input_num, reverse=True)
print(f'Original: {list_output}')

for number in list_output:
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(f'The prime numbers: {number}')
            break
