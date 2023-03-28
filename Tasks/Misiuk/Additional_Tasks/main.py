import os
list_file = os.listdir(path='.')
dict_output = {}

if len(list_file) != 1:
    for name in list_file:
        if name[-3::] == 'txt':
            with open(name, 'r') as file:
                for item in file:
                    content = item.lower().replace(',', '').replace('.', '').replace('?', '').split()
                    for word in content:
                        if word in dict_output:
                            dict_output[word] += 1
                        else:
                            dict_output[word] = 1
    for key, elem in dict_output.items():
        print(f'Слова найденные в файлах "{key}" - количество {elem}')
else:
    print('Файлов для чтения не найдено!!!!\nИспользуйте файлы с расширением .txt')
