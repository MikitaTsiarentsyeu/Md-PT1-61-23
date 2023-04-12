while True:
    UserLimit = input("Введите максимальное количество символов в строке (больше 35):\n")
    if UserLimit.isdigit():
        UserLimit = int(UserLimit)
        if UserLimit <= 35:
            print("Количество должно быть больше 35") 
        else:
            break
    else:
        print("Неверный тип данных")


with open('Tasks/!!!Tasks/Task4/text.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()
    new_text = ""
    ContentList=content.split()
    LineLen = 0
    for words in ContentList:
        WordLen = len(words)
        if LineLen + WordLen >= UserLimit:
            new_text += '\n'
            LineLen = 0  
        new_text += words + " "
        LineLen += WordLen + 1

with open('Tasks/Nikiforov/Task4/Task.txt', 'w', encoding = 'utf-8') as f:
    f.write(new_text)

with open('Tasks/Nikiforov/Task4/Task.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

new_content = ""
for line in lines:
    line = line.rstrip()
    line = line + "\n"
    lack = UserLimit +1 - len(line)
    AmountSpaces = line.count(" ")
    if AmountSpaces == 0:
        new_content += line
        continue
    proportion = lack // AmountSpaces
    DecimalPart = lack % AmountSpaces
    NewSpaces = " " * (proportion+1)
    line = line.replace(" ", NewSpaces)
    if DecimalPart > 0:
        line = line.replace(NewSpaces, NewSpaces + " ", DecimalPart)
    new_content += line

with open('Tasks/Nikiforov/Task4/Task4.txt', 'w', encoding = 'utf-8') as f:
    lines = f.writelines(new_content)
    print("Готово, проверь файл Task4.txt")






