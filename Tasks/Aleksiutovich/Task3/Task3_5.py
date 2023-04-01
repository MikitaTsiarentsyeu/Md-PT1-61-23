#Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
strings = ["OxY", "OxYgen", "Starvation", "This is I", "The"]
def filter_str(str_x):
    res = []
    for x in str_x:
        if len(x) > 5:
            res.append(x)
    return res

filter_strings = filter_str(strings)
print(filter_strings)