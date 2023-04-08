while True:
    max = input("Введите число максимального количества символов в строке (больше 35)!\n")
    if  max.isalpha():
        print("Вводить можно только числа.")
        continue
    if int(max) <= 35:
        print("Число должно быть больше 35.")
        continue
    if int(max)> 35:
        break
max = int(max)
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
with open("new_text.txt", "w", encoding="utf-8") as file:
    str = ""
    count = 0 
    new_text = ""
    for string in text.split("\n"):
            for word in string.split():
                count += len(word)
                if count >= max:
                    str += "\n"
                    count = len(word)
                elif str != "":
                    str += " "
                    count += 1
                str += word    
            for y in str.split("\n"):
                s = max - len(y)
                while len(y) < max:
                    y = y.replace(" ", "  ",s)
                    s = max - len(y)
                    if s > len(y):
                        break
                new_text += (y + "\n")
                str = ""
                count = len(word)
    file.writelines(new_text)
print("Отредактированный текст записан в new_text.txt")
