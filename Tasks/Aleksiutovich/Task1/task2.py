import math
#Write a program that calculates the area of a circle given its radius.
def the_area_circle():
    print("Program that calculates the area of a circle given its radius")
    # introducing the variable radius
    r = float(input("Please enter the radius of the circe: "))
    area = r ** 2 * math.pi

    print(f" The area of the given circe is {round(area, 2)}")
    
    return area


    
the_area_circle()