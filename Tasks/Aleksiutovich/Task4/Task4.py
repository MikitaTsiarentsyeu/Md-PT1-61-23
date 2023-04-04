# -*- coding: utf-8 -*-

def format_text(file):
    max_num_lines = int(input("Введите максимальное количество символов в строке  \n >"))

    if max_num_lines < 35:
        print("Внимание!!!Принимается значение не менее 35!")
        print("Повторите ввод!")

    else:
# max_num_lines = 40
        lists = []
        with open(file) as f:
            for line in f:
                lists.append(line.split())
        lines = []
        current_line = ''
        for list in lists:
            for word in list:
                if len(current_line) + len(word) + 1 <= max_num_lines:
                    current_line += word + ' '
                else:
                    lines.append(current_line)
                    current_line = word + ' '
            lines.append(current_line)
            current_line = ''
        with open('format_file.txt', 'w') as new_f:
            new_f.write('\n'.join(lines))
            print("Файл создан и удачно записан!")

text = 'text.txt'
format_text(text)
