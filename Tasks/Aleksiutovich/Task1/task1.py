#Write a program that converts Celsius to Fahrenheit
def the_converts_C_to_F():
    print("It is a simple converter of degrees Celsius to Fahrenheit")
    print("Enter the temperature value in Celsius")
    
    celsius = float(input("Celsius: "))
    fahrenheit =  celsius * 9/5  + 32
    
    print(f"Fahrenheit: {fahrenheit}")
    
    return fahrenheit

the_converts_C_to_F()