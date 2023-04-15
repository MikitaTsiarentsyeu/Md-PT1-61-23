

while True:
    max = int(input("Введите максимальное количество символов в строк, оно должно быть больше 35: \n"))
    if max <= 35:
        print("Количество должно быть больше 35.")
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
                if count >= max:
                    str += "\n"
                    count = len(word)
                elif str != "":
                    str += " "
                    count += 1
                str += word    
            for j in str.split("\n"):
                s = max - len(j)
                while len(j) < max:
                    j = j.replace(" ", "  ",s)
                    s = max - len(j)
                    if s > len(j):
                        break
                new_text += (j + "\n")
           
    file.writelines(new_text)
    print("Отредактированный текст записан в new_text.txt")

    
