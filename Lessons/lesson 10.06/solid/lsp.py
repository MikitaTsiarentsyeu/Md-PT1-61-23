class Rectangle:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b
    
class Square(Rectangle):

    def __init__(self, a) -> None:
        super().__init__(a, a)

    # def area(self):
    #     return super().area()

s = Rectangle(3)
s.area()