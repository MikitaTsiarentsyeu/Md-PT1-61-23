import os

path = "test level 1\\test level 2\\test level 3"

separator = '\\' if os.name == 'nt' else '/'
print(separator)
print(os.name)

print(os.sep)

levels = ["test level 1", "test level 2", "test level 3"]
print(os.sep.join(levels))

new_dir = os.path.join(*levels)

print(os.getcwd())

# os.chdir("lesson 02.04")

# open("test.txt", "w")

# os.makedirs(new_dir)

# print(os.listdir())

for l in os.walk(os.getcwd()):
    print(l)

os.removedirs(new_dir)
os.remove("test.txt")