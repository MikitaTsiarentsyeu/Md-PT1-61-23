def input_int(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print('Input integer!')


while True:
    symbols_in_line = input_int('Input maximal number of symbols in line (>35): ')
    if symbols_in_line <= 35:
        print('Number should be more than 35')
    else:
        break

lines = []

with open('text.txt', 'r') as file:
    while True:
        line = file.readline()
        lines.append(line.split())
        if not line:
            break

del lines[-1]  # lines[-1] == []

paragraphs = []
new_line = ''

for line in lines:
    paragraph = []
    for word in line:
        if len(new_line) + len(word) + 1 > symbols_in_line:
            paragraph.append(new_line.strip())
            new_line = word + ' '
        else:
            new_line = new_line + word + ' '
    paragraph.append(new_line)
    new_line = ''
    paragraphs.append(paragraph)

lines_to_write = []

for par in paragraphs:
    for line in par:
        difference = symbols_in_line - len(line)
        while difference > 0:
            temp_length = len(line)
            if line[-1] == ' ':
                lines_to_write.append(line)
                break
            line = line.replace(' ', '  ', difference)
            difference -= (len(line) - temp_length)
            if difference == 0:
                lines_to_write.append(line)
                break

with open('new_text.txt', 'w') as new_file:
    for line in lines_to_write:
        new_file.write(line + '\n')
    print('Information is successfully written in the new file!')
