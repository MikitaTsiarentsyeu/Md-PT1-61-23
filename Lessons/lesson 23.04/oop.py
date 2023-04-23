
class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.__breed = breed

    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = Dog.__convert_name(name)

    def __convert_name(name):
        return name.strip().upper()

    name = property(get_name, set_name)
    breed = property(get_breed)


    def bark(self):
        print("woof!")

    def bark_the_name(self):
        print(self.__name)

    

# Dog.bark()
# print(Dog.name)
# print(Dog.breed)

print(type(Dog))
print(type(2), type(int))

zephyrka = Dog("Zephyrka", "wss")
print(type(zephyrka))
max = Dog("Max", "corgi")
print(zephyrka.name)
print(zephyrka.breed)
print(max.name)
print(max.breed)

zephyrka.bark()
max.bark()

Dog.bark(zephyrka)
Dog.bark(max)

zephyrka.bark_the_name()
max.bark_the_name()

max.name = "megamax"
print(max.name)
max.breed = "german shepherd"
# print(max._Dog__breed)
