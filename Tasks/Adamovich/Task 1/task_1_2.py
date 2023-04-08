#2. Write a program that calculates the area of a circle given its radius.
import math
area_of_circle = float(float(input("Input radius of circle: ")) **2 * math.pi)
print(f" The area of a circle is {round(area_of_circle,2)}")