#Write a program that converts kilometers per hour to meters per second, given the speed in kilometers per hour.
def the_convert_Kmph_to_Mps():
    print("Program to convert Kilometers per hour to Meters per second")
    
    val_Kmph = float(input("Please enter value the speed in kilometers/hour: "))
    val_Mps = ( val_Kmph * 1000 ) / 3600
    
    print(f"The speed is {round(val_Mps, 2)} m/sec")
    
    return val_Mps

the_convert_Kmph_to_Mps()