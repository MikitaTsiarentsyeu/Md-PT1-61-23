x = int(input("Enter the x value:\n"))
y = int(input("Enter the y value:\n"))

try:
    try:
        if y == 0:
            raise RuntimeError("The y value is 0")
        print(res)
        res = x/y
        print(res)
    # except Exception:
    #     print("ooooops")
    except ZeroDivisionError:
        print("division be zero")
        y = int(input("Enter the new y value:\n"))
        res = x/y
        print(res)
    except NameError as ne:
        print(type(ne))
        print(ne)
        print(id(ne))
        print("cannot find your data")
        raise ne
    except:
        print("something went wrong")
    else:
        print("nothing went wrong")
except Exception as e:
    print(id(e))
    print("something went wrong")

print("the end")