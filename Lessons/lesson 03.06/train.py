
class FreightTrain:

    cart_len = 10

    def __init__(self, count) -> None:
        self.cart_len = count

    def __str__(self) -> str:
        return f"I'm a train of {self.cart_len} carts, choo-choo!"

    def __int__(self):
        return self.cart_len
    
    def __add__(self, other):
        """the add method should suport both FreightTrain and int data types"""
        if not isinstance(other, int) and not isinstance(other, FreightTrain):
            raise TypeError(f"cannot add {type(other).__name__} object")
        if isinstance(other, int):
            return FreightTrain(self.cart_len+other)
        return FreightTrain(self.cart_len + other.cart_len)
    
    # def __add__(self, other):
    #     try:
    #         return FreightTrain(self.cart_len + other.cart_len)
    #     except AttributeError:
    #         raise TypeError(f"cannot add {type(other).__name__} object")

    def __len__(self):
        return self.cart_len
    
    def __eq__(self, __value: object) -> bool:
        # if not isinstance(__value, FreightTrain):
        #     return False
        
        try:
            return self.cart_len == __value.cart_len
        except AttributeError:
            return False

shorty = FreightTrain(5)
looong = FreightTrain(100)
print(int(shorty))

print(shorty + looong)
shorty.__add__(looong)
print(looong + shorty)
looong.__add__(shorty)

print(shorty + 50)
shorty.__add__(50)

# shorty+50.0

print(len(shorty + looong))