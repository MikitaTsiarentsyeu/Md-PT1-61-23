from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

class Eater(ABC):

    @abstractmethod
    def eat(self):
        pass

class Developer(Worker):

    def work(self):
        print("writing some code...")

    # def eat(self):
    #     print("having lunch...")

class Manager(Worker):

    def work(self):
        print("managing tasks...")

    # def eat(self):
    #     print("having lunch...")