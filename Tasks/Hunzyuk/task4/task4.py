length = int(input("Enter string length (>35) "))


with open("text.txt", "r", encoding="utf-8") as file:
    content = []
    res =  ""

    for string in file:
        content.append(string.strip().split())

    lst = []
    
    for string in content: 
        for word in string:
            if len(res) + len(word) + 1 <= length:
                    res += word + " "
            else:
                while True:
                    if len(res) <= length:
                        res = res.replace(' ', '  ', length - len(res)).strip() 
                        if len(res) == length:               
                            lst.append(res)
                            break
                res = word + " "
            
        lst.append(res)
        res = ''



with open('new_text.txt', 'w', encoding='utf-8') as file:
    file.writelines('\n'.join(lst))
    print('File formatted successfully')





