class MathUtils:

    @staticmethod
    def sum(a, b):
        return a+b
    
    @staticmethod
    def create_circle(radius):
        return MathUtils.__Circle(radius)
    
    @staticmethod
    def create_rectangle(length, width):
        return MathUtils.Rectangle(length, width)
    
    @staticmethod
    def create_square(width):
        return MathUtils.Rectangle(width, width)


    class __Circle:

        def __init__(self, radius) -> None:
            self.radius = radius
        
        def __str__(self) -> str:
            return f"{MathUtils.__Circle.__name__}({self.radius})"
        
    class Rectangle:

        def __init__(self, length, width) -> None:
            self.length = length
            self.width = width

        def __str__(self) -> str:
            return f"Rectangle({self.length}, {self.width})"


print(MathUtils.sum(2, 3))