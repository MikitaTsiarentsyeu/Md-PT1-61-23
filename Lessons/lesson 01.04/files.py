# f = open('test.txt', 'w')
# print(type(f), f)
# f.write("test new file")
# f.close()

with open('test.txt', 'w') as f:
    f.write("test new file\n")
    f.write("some additional info\n")
    f.writelines(['line 1\n', 'line 2\n', 'line 3\n'])


with open('test.txt', 'r') as f:
    for line in f:
        print(repr(line))
    # print(f.readlines())
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.read(1000)))
    # f.seek(0)
    # print(repr(f.read(1000)))
    # print(repr(f.read(1000)))

with open('test.txt', 'a') as f:
    f.write("new text from append\n")
    # f.read() error

with open('test.txt', 'a+') as f:
    f.seek(0)
    f.write("new text from a+\n")
    print(f.read())

with open('test.txt', 'r+') as f:
    f.write("prepended content")
    print(repr(f.read()))

with open('test.txt', 'w+') as f:
    f.write("prepended content")
    f.seek(0)
    f.write("test")
    print(repr(f.read()))