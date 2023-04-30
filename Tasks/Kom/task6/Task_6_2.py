def read_file(name_file:str)->str:
    try:
        with open(name_file,'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'File not found'

def file_selection():
    print('Choose a file to read:')
    print('1. Tasks.txt')
    print('2. Tasksz.txt')

    try:
        num_file = int(input('File number:\n'))
        if num_file == 1:
            print(read_file('Tasks.txt'))
        elif num_file == 2:
            print(read_file('Tasksz.txt'))
        else:
            print('You selected a non-existent value.')
    except:
        print('Error - exit this program!!!')

file_selection()