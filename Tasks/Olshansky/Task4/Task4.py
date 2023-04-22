# 1. Подготовиться к чтению содержимого файла text.txt
# 2. Дать пользователю ввести с клавиатуры условный параметр "максимальное количество символов в строке",
# который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов, при этом
# если слово целиком не умещается в строке, оно должно быть перенесено на следующую,
# а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)

while True:
    str_length = int(input("Please input desirable string length (>35): \n"))
    if str_length <= 35:
        print("The length should be more than 35, try again")
        continue
    else:
        break

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
with open("new_text.txt", "w", encoding="utf-8") as file:
    str = ""
    count = 0
    new_text = ""
    for string in text.split("\n"):
        for word in string.split():
            count += len(word)
            if count >= str_length:
                str += "\n"
                count = len(word)
            elif str != "":
                str += " "
                count += 1
            str += word
        for j in str.split("\n"):
            s = str_length - len(j)
            while len(j) < str_length:
                j = j.replace(" ", "  ", s)
                s = str_length - len(j)
                if s > len(j):
                    break
            new_text += (j + "\n")

    file.writelines(new_text)
    print("Your file 'new_text.txt' was successfully created")
