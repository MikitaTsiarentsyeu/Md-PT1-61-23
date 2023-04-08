width = int(
    input('Enter maximum number of characters per line but not less than 35:\n'))
sum_line = 0
list_write = []
while width < 35:
    print('You entered the wrong number, please try again')
    width = int(
        input('Enter maximum number of characters per line but not less than 35:\n'))

with open('text.txt', 'r') as file:
    with open('text_output.txt', 'w') as file_out:
        for line in file.readlines():
            if file_out.tell() != 0:
                file_out.write('\n')
            for j in line.split():
                sum_line += len(j) + 1
                if sum_line > width:
                    list_write[-1] = list_write[-1].replace(' ', '\n')
                    while sum_line - len(j) - 1 != width:
                        for i in range(0, len(list_write)-1):
                            if sum_line - len(j) - 1 == width:
                                break
                            list_write[i] += ' '
                            sum_line += 1
                    file_out.writelines(list_write)
                    list_write.clear()
                    sum_line = len(j) + 1
                if sum_line <= width:
                    list_write.append(j + ' ')
                    continue
            list_write[-1] = list_write[-1].replace(' ', '')
            file_out.writelines(list_write)
            sum_line = 0
            list_write.clear()

print('\nThe file is saved in this directory.')
print('------------------------------------')
print('File name: text_output.txt\n')
