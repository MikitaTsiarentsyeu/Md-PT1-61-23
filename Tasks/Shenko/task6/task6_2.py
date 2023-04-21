# Напишите функцию, которая читает файл и возвращает его содержимое в виде строки. 
# Обработайте FileNotFoundError и верните «Файл не найден», если файл не существует. 

def file_read():
    try:
        with open("test.txt", "r") as f:  
            return(f.readline())
    except FileNotFoundError:
        print("File not found")
print(file_read())

