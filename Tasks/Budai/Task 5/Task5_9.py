def calculate_power(n, power):
    if n == 0:
        return 1
    if power >= 0:
        if power == 0:
            return 1
        else:
            return n * calculate_power(n, power - 1)
    else:
        power = -1 * power
        return 1 / (n * calculate_power(n, power - 1))


number = int(input('Input number: '))
power = int(input('Input power: '))

print(f'{number} ** {power} = {calculate_power(number, power)}')
