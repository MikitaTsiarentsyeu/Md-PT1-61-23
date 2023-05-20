class Proto:

    def __init__(self, proto_param) -> None:
        self.proto_param = proto_param

    def __str__(self) -> str:
        return "my unique str concept for proto"

class Parent(Proto):

    def __init__(self, proto_param, param1, param2) -> None:
        super().__init__(proto_param)
        self.param1 = param1
        self.param2 = param2

    parent_atr = "parent"

    def parent_method(self):
        print("the parent method")

class Child(Parent):

    def __init__(self, proto_param, param1, param2, param3) -> None:
        super().__init__(proto_param, param1, param2)
        self.param3 = param3

    parent_atr = "child"

    def child_method(self):
        print("the child method")

    def parent_method(self):
        Parent.parent_method(self)
        print("the child parent method")

print(Child.__dict__)

child = Child(0,1,2,3)
print(child.__dict__)


child.parent_method()
child.child_method()
print(child.parent_atr)
print(child)