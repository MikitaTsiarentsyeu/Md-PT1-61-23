a = []
def sum_numbers():
    try:
        total = 0
        for i in a:
            if i % 2 == 0:
                total += i
        print(total)
    except TypeError:
        print("Invalid input type")
        
a = [2, 5, 10, 15, 20, 100]
sum_numbers()
a = "привет"
sum_numbers()
a = [2, 5, "привет"]
sum_numbers()
a = "2, 5, 10, 20"
sum_numbers()
