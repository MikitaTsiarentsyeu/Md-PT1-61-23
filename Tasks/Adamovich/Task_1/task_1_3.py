# 3. Write a program that converts kilometers per hour to meters per second, given the speed in kilometers per hour.
speed_kilometers_meters_per_hour = float(input("Input speed in kilometers per hour: "))
speed_meters_per_second = float((speed_kilometers_meters_per_hour * 5) / 18)
print(f" {speed_kilometers_meters_per_hour} kilometers per hour is {round(speed_meters_per_second, 2)} meters per second")