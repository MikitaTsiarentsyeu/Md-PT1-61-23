# -*- coding: utf-8 -*-

def format_text(file):
    max_num_lines = int(input("""Enter the maximum number of characters per line.
The number must be greater than 35.
\\> """))

    if max_num_lines < 35:
        print("Attention. A value of at least 35 is accepted.")
        print("Error. Repeat the input.")
        raise ValueError("Invalid input! Number must be at least 35.")

    else:
        # max_num_lines = 40
        lists = []
        with open(file) as f:
            for line in f:
                lists.append(line.strip().split())
        lines = []
        current_line = ''
        for list_ in lists:
            for word in list_:
                if len(current_line) + len(word) + 1 <= max_num_lines:
                    current_line += word + ' '
                else:
                    lines.append(current_line[:-1])  # .ljust(max_num_lines)
                    current_line = word + ' '
            lines.append(current_line[:-1])  # .ljust(max_num_lines)
            current_line = ''
        new_lines = []
        for line in lines:
            print(len(line))
            if len(line) == max_num_lines:
                new_lines.append(line.ljust(max_num_lines))
            elif len(line) < max_num_lines:
                y = max_num_lines - len(line)
                line = line.replace(' ', '  ', y)
                new_lines.append(line)

        print(lines)
        print(new_lines)

        with open('format_file.txt', 'w') as new_f:
            new_f.write('\n'.join(new_lines))
            print("The file has been created and successfully recorded.")


text = 'text.txt'
format_text(text)
