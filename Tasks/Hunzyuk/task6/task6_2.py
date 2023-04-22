def read_file(file):
    try:
        with open(file, 'r') as f:
            res = f.read()
            return res
    except FileNotFoundError:
        return f"File not found"
    
print(read_file('test1.txt'))