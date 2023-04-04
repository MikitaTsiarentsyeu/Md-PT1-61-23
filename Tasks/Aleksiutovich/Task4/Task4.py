# -*- coding: utf-8 -*-

def format_text(file):
    max_num_lines = int(input("""Enter the maximum number of characters per line.
The number must be greater than 35.
\\>"""))

    if max_num_lines < 35:
        print("Attention!!!A value of at least 35 is accepted!")
        print("Error! Repeat the input!")

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
            print("The file has been created and successfully recorded!")


text = 'text.txt'
format_text(text)
