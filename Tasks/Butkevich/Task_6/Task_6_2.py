# 2. Write a function that reads a file and returns its contents as a string. Handle the FileNotFoundError and return
# "File not found" if the file does not exist.


def read_file(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    except FileNotFoundError:
        return "File not found"


print(read_file("Text_for_task_6_2.txt"))


