class MathUtils:

    pi = 3.14

    @classmethod
    def add(cls, a, b):
        return a+b
    
    @classmethod
    def circle_area(cls, r):
        return cls.pi*r**2
    
print(MathUtils.add(2, 3))

mu = MathUtils()
print(mu.add(2,3))

MathUtils.circle_area(1)