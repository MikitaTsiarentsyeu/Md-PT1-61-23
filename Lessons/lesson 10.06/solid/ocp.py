from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b
    
class Circle(Shape):

    def __init__(self, r) -> None:
        self.r = r

    def area(self):
        return 3.14*self.r*self.r

