while True:
    val = input("Input your time value in the format hh:mm\n")
    
    if len(val) != 5:
        print("the length of your value is incorrect, please try again")
        continue

    if val[2] != ':':
        print("your value misses the : sign, please try again")
        continue

    hours, minutes = val.split(':')

    if not hours.isdigit():
        print("the hours value must be digital, please try again")
        continue

    if not minutes.isdigit():
        print("the minutes value must be digital, please try again")
        continue

    hours = int(hours)
    minutes = int(minutes)

    if (hours < 0) or (hours > 23):
        print("the hours value must be from 0 to 23, please try again")
        continue

    if (minutes < 0) or (minutes > 59):
        print("the hours value must be from 0 to 23, please try again")
        continue

    break

print("The main logic goes here")