def read_file(filename):
    try:
        file = open(filename, 'r')
        res = ''
        for line in file.readlines():
            res += line.replace('\n', ' ')
        file.close()
        return res
    except FileNotFoundError:
        return 'File not found'


print(read_file('test.txt'))
print(read_file('test2.txt'))
