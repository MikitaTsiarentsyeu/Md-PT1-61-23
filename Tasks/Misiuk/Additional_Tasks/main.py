import os
list_file = [x for x in os.listdir('.') if x.endswith(('.txt'))]

dict_output = {}
signs = [',', '.', '!', '?', ':', ';', '"',
         "'", '#', '%', '@', '$', '^', '*', '<', '>']

if list_file:
    for name in list_file:
        with open(name, 'r') as file:
            for item in file:
                for i in signs:
                    item = item.lower().replace(i, ' ')
                for word in item.split():
                    if word in dict_output:
                        dict_output[word] += 1
                    else:
                        dict_output[word] = 1
    for key, elem in dict_output.items():
        print(f'Слова найденные в файлах "{key}" - количество {elem}')
else:
    print('Файлов для чтения не найдено!!!!\nИспользуйте файлы с расширением .txt')
