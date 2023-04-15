def prepare():
    print("preparing a base")
    print("choosing a sauce")

def add_ingridient(ingrifient):
    print(f"adding {ingrifient}")

def grind_cheese():
    print("grinding cheese")

def bake(t, time):
    print(f"baking at {t} gegrees at {time} minutes")

def done():
    print("boxing")
    print("slicing")
    print("done!")


# def make_pepperoni():
#     prepare()
#     add_ingridient('pepperoni')
#     grind_cheese()
#     bake(200, 10)
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient('pepperoni')
#     add_ingridient('pepperoni')
#     grind_cheese()
#     bake(200, 10)
#     done()

# def make_gawaii():
#     prepare()
#     add_ingridient('chicken')
#     add_ingridient('pineapple')
#     grind_cheese()
#     bake(180, 12)
#     done()

def pizza_factory(ingridients, t, time):
    def inner():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        bake(t, time)
        done()
    
    return inner

make_pepperoni = pizza_factory(['pepperoni'], 200, 10)
make_double_pepperoni = pizza_factory(['pepperoni', 'pepperoni'], 200, 10)
make_gawaii = pizza_factory(['chicken', 'pineapple'], 180, 12)

make_gawaii()