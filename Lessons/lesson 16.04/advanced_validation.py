while True:
    value = input("Input your time in the format hh:mm\n")

    try:
        if len(value) != 5:
            raise RuntimeError("The hours and minutes should be set as two digits")
        h, m = value.split(':')
        h, m = int(h), int(m)
        if h < 0 or h > 23:
            raise RuntimeError("The hour value must be in range from 0 to 23")
        if m < 0 or m > 59:
            raise RuntimeError("The minute value must be in range from 0 to 59")
        break
    except RuntimeError as e:
        print(e)
        continue
    except ValueError:
        print("Only numbers should be used in the format")
        continue

print("the main logic goes here")