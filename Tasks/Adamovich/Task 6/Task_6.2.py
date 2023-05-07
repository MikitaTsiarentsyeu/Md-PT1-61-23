#2. Write a function that reads a file and returns its contents as a string. Handle the FileNotFoundError and return "File not found" if the file does not exist.

def read_file(file):
 try:
    with open(file, 'r') as f:
        content = f.read()
    return content
 except FileNotFoundError:
    print("File not found")


print(read_file("text_for_task_6.2.txt"))

