# -*- coding: utf-8 -*-
# Write a function that reads a file and returns its contents
# as a string. Handle the FileNotFoundError
# and return "File not found" if the file does not exist.
def read_file(file):
    result = ''
    try:
        list_tmp = []
        with open(file) as f:
            list_tmp = f.readlines()

        def inner():
            nonlocal result
            for str_list in list_tmp:
                result += ''.join(str_list)
            return result

        return inner()
    except FileNotFoundError:
        return "File not found"


# test
# file = 'file1.txt'
file = 'file.txt'
res = read_file(file)
print(res)
