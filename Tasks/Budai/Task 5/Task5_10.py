def find_fibonacci_number(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return find_fibonacci_number(n-1) + find_fibonacci_number(n-2)


sequence_number = int(input('Input sequence number: '))

print(f'{sequence_number} number in Fibonacci sequence is {find_fibonacci_number(sequence_number)}')
