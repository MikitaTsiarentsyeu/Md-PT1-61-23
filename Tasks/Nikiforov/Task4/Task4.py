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
    print("Готово, проверь файл Task.txt")

# Не получается с выравниванием, что я делаю не так?

# with open('Tasks/Nikiforov/Task4/Task.txt', 'r', encoding = 'utf-8') as f:
#     lines = f.readlines()
  
# for i in range(len(lines)):
#     if len(lines[i]) < UserLimit:
#         words = lines[i].split()
#         delta = UserLimit - len(lines[i].strip())
#         gap = len(words) - 1
#         if gap > 0:
#             SpacesPerGap = delta // gap
#             ExtraSpaces = delta % gap
#             for j in range(gap):
#                 words[j] += " " * SpacesPerGap
#                 if ExtraSpaces > 0:
#                     words[j] += " "
#                     ExtraSpaces -= 1
#         lines[i] = ' '.join(words)

# with open('Tasks/Nikiforov/Task4/Task.txt', 'w', encoding = 'utf-8') as f:
#     lines = f.writelines(lines)









