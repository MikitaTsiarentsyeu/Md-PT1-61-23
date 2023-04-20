def read_file(a):
    try:
        with open(a) as f:
            new_file = f.read()
            print(new_file)
    except FileNotFoundError:
        print("File not found")
a = "text.txt"
read_file(a)

a = "text_one.txt"
read_file(a)
    