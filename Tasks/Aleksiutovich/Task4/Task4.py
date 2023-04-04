# -*- coding: utf-8 -*-


def format_text(list_, max_chars):
    """

    :param list:  одномерный список из слов
    :param max_chars:  максимальное количество символов в строке
    :return: отформатированный текст
    """
    num = len(list_)
    lines = []
    line = []
    line_len = 0
    for x in list_:
        line.append('\t')
        for word in x:
            if line_len + len(word) + len(line) > max_chars:
                for y in range(len(line)):
                    line[y] += ' '
                    if y < max_chars - line_len:
                        line[y] += ''
                lines.append(' '.join(line))
                line = []
                line_len = 0
            line.append(word)
            line_len += len(word)
        line.append('\n')
    lines.append(" ".join(line))
    return '\n'.join(lines)


def task_4(file):
    """

    :param file: Файл с текстом
    :return: Записывает новый отфарм. файл
    """
    # max_num_lines = int(input("Enter maximum number of characters per line \n >"))
    # if max_num_lines < 35:
    #     print("Внимание!!!Принимается значение не менее 35!")
    #     print("Повторите ввод")
    #     task_4()
    # else:

    max_num_lines = 40
    lines_ = []
    with open(file) as f:
        # cont = f.read()
        # words = cont.split()
        for line in f:
            lines_.append(line)

    # print(lines_)
    for x in range(len(lines_)):
        lines_[x] = lines_[x].split()
    # print(lines_)
    new_f = open('format_file.txt', 'w')
    new_f.write(format_text(lines_, max_num_lines))
    new_f.close()
    print(format_text(lines_, max_num_lines))


text = 'text.txt'
task_4(text)
