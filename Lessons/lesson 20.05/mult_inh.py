class RunningAnimal:

    def run(self):
        print("I'm running")

class FlyingAnimal:

    def fly(self):
        print("I'm flying")

class SwimmingAnimal:

    def swim(self):
        print("I'm swimming")

class Pinguin(RunningAnimal, SwimmingAnimal):

    pass


class Food:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

class Animal:

    def eat(self, obj:Food):
        print(f"eating {obj.name}")

    def phe(self):
        print("pheeeeee")

class Carnivore(Animal):

    def eat(self, obj: Food):
        if obj.type == "meat":
            Animal.eat(self, obj)
        else:
            super().phe()

class Herbivore(Animal):

    def eat(self, obj: Food):
        if obj.type == "plant":
            Animal.eat(self, obj)
        else:
            super().phe()

class Omnivore(Herbivore, Carnivore): pass

meat = Food("stake", "meat")
plant = Food("grass", "plant")

c = Carnivore()
h = Herbivore()
o = Omnivore()

food = [meat, plant]
eaters = [c, h, o]

# for eater in eaters:
#     for f in food:
#         eater.eat(f)

o.eat(plant)
print(Omnivore.__mro__)