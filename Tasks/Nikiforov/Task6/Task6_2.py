# 2. Write a function that reads a file and returns its contents as a string.
# Handle the FileNotFoundError and return "File not found" if the file does not exist.

file_link = 'Tasks/Nikiforov/Task6/Task6_1.py'
wrong_link = 'Tasks/Nikiforov/Task6/Task6_1.txt'

def file_reads(f_link):
    try:
        with open(f_link, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "File not found"
    
print(f"{file_link}:\n{file_reads(file_link)}")
print(f"{wrong_link}:\n{file_reads(wrong_link)}")