def input_list_of_numbers():
    while True:
        try:
            numbers = list(map(int, input('Input numbers: ').split()))
            return numbers
        except ValueError:
            print('Incorrect input! Input integers!')
