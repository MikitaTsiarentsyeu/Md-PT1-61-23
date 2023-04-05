# -*- coding: utf-8 -*-
def align_to_width_str(line, width):
    words = line

    # print(words)
    num_spaces = width - sum(len(word) for word in words)
    if len(words) == 1:
        return words[0] + ' ' * num_spaces

    space_counts = [1] * (len(words) - 1)
    while sum(space_counts) < num_spaces:
        for i in range(len(space_counts)):
            space_counts[i] += 1
            if sum(space_counts) == num_spaces:
                break
    new_line = ''
    for word, space_count in zip(words, space_counts):
        new_line += word + ' ' * space_count
    new_line += words[-1]
    # print(new_line)
    return new_line


def format_text(file):
    """
    This function opens a text file, formats it according
    to the length of the line that it requests from the user.
     And writes the formatted text to a new file.
    Parameter:
        file -- The str indicating the path to the file

    """
    # Запрос максимальной длины строки
    max_num_lines = int(input("""Enter the maximum number of characters per line.
The number must be greater than 35.
\\>>> """))

    # Проверка правильности ввода максимальной длины
    if max_num_lines < 35:
        print("Attention. A value of at least 35 is accepted.")
        print("Error. Repeat the input.")
        raise ValueError("Invalid input! Number must be at least 35.")

    # Если введенная максимальная длина верна, то приступаем к форматированию файла
    else:
        # Создаем список для хранения строк исходного файла
        lists = []
        # Открываем файл и записываем его строки в созданный список
        with open(file) as f:
            for line in f:
                lists.append(line.strip().split())
        # Создаем список для хранения отформатированных строк
        lines = []
        # Создаем список для хранения слов текущей строки
        current_line = []
        # Обходим все строки исходного файла
        for list_ in lists:

            # Обходим каждое слово в строке
            for word in list_:
                if len(' '.join(current_line)) + len(word) <= max_num_lines:
                    # Если длина текущей строки плюс длина
                    # следующего слова меньше максимальной длины строки,
                    # то добавляем это слово в текущую строку
                    current_line.append(word)
                else:
                    # Если длина текущей строки плюс длина следующего
                    # слова больше максимальной длины строки,
                    # то записываем текущую строку
                    # в список строк и начинаем новую строку
                    lines.append(current_line)
                    current_line = [word]
            # Добавляем текущую строку в список строк
            # print(lines)
            lines.append(current_line)

            # Обнуляем текущую строку
            current_line = []
        # Создаем список для хранения окончательно отформатированных строк
        new_lines = []
        # Обходим все строки
        for line in lines:
            #
            new_lines.append(align_to_width_str(line, max_num_lines).rstrip())
            # # Если длина строки равна максимальной длине,
            # # то сохраняем ее как есть
            # if len(' '.join(line)) == max_num_lines:
            #     new_lines.append(' '.join(line))
            # # Если длина строки меньше максимальной длины,
            # # добавляем пробелы между словами,
            # # чтобы длина строки стала равна максимальной длине
            # elif len(' '.join(line)) < max_num_lines:
            #     num_spaces = max_num_lines - len(''.join(line)) + 1
            #     # space_counts количество пробелов
            #     space_counts = [1] * len(line)
            #     # Увеличиваем значение индексов,
            #     # пока сумма space_counts не сравнится с num_spaces
            #     while sum(space_counts) < num_spaces:
            #         for i in range(len(space_counts)):
            #             space_counts[i] += 1
            #             if sum(space_counts) == num_spaces:
            #                 break
            #
            #     new_line = ''
            #     # Обьединяем текущее слово с количеством пробелов,
            #     # и добавляем все это в new_line.
            #     for word, space_count in zip(line, space_counts):
            #         new_line += word + ' ' * space_count
            #
            #     # Удаляем все конечные пробелы и добавляем к списку
            #     new_lines.append(new_line.rstrip())

        # Создаем новый файл с отформатированными строками и закрываем его
        with open('formated_file.txt', 'w') as new_f:
            new_f.write('\n'.join(new_lines))
        # Оповещаем  об этом пользователя
        print("The file has been created and successfully recorded.")


file_now = 'text.txt'
format_text(file_now)
# format_text_tw(file_now)
