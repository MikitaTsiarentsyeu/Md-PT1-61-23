
class InvertedStack:

    def __init__(self, *items) -> None:
        self.__items = []
        if items:
            self.__items.extend(items)
            
    # def get_items(self): VERY BAD APPROACH, NEVER USE IT
    #     return self.__items

    def pop(self):
        try:
            return self.__items.pop(0)
        except IndexError:
            return
        
    def push(self, obj):
        self.__items.insert(0, obj)

    def __iter__(self):
        return self
    
    def __next__(self):
        item = self.pop()
        if item:
            return item

        raise StopIteration
    
    def __str__(self) -> str:
        return f"{InvertedStack.__name__}({','.join([str(x) for x in self.__items])})"
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, InvertedStack):
            return False
        
        return self.__items == __value.__items

stck = InvertedStack(1,2,3,4,5)
print(stck)
# print(stck.get_items())
# stck.get_items().append(6)
# print(stck.get_items())
print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
stck.push(11.1)
stck.push("test obj")
print(stck.pop())
print(stck.pop())
print(stck.pop())

stck = InvertedStack(1,2,3,4,5)
print(iter(stck))

for i in stck:
    print(i)

print(stck.pop())
stck.push([1,2,3])
stck.push("test")
print(stck)

# stck.push(stck)
# print(stck)