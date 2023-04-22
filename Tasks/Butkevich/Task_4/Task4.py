def format_text(number: int) -> int:
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()
    with open("my_text_txt", "w", encoding="utf-8") as file:
        str = ""
        count = 0
        my_text = ""
        for string in text.split("\n"):
            for word in string.split():
                count += len(word)
                if count >= number:
                    str += "\n"
                    count = len(word)
                elif str != "":
                    str += " "
                    count += 1
                str += word
            for y in str.split("\n"):
                s = number - len(y)
                while len(y) < number:
                    y = y.replace(" ", "  ", s)
                    s = number - len(y)
                    if s > len(y):
                        break
                my_text += (y + "\n")
                str = ""
                count = len(word)
        file.writelines(my_text)
        return "New file created"


while True:
    number = input()
    if number.isalpha():
        print("You have to enter a number")
        continue
    if int(number) <= 35:
        print("Number must be greater than 35")
        continue
    if int(number) > 35:
        break

print(format_text(int(number)))
