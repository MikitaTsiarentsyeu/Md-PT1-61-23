from abc import abstractmethod, ABC

class Animal(ABC):

    @abstractmethod
    def SaySomething(self):
        print("Hello, I'm an animal!")

class Dog(Animal):

    def SaySomething(self):
        print("woof!")

class Cat(Animal):

    def SaySomething(self):
        print("nyaaa!")

class Human:

    def SaySomething(self):
        print("Hello, I'm human and it sounds proudly")

class Croc(Animal):

    def SaySomething(self):
        return super().SaySomething()

# a = Animal()
d = Dog()
c = Cat()
h = Human()
croc = Croc()

def say(*animals):
    for animal in animals:
        # if hasattr(animal, "SaySomething"):
        #     animal.SaySomething()
        try:
            animal.SaySomething()
        except AttributeError:
            continue

say(d, c, h, croc, object)