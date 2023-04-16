SECRET = "test_secret"

def check_user(func):
    def wrapper():
        key = input("Enter the secret key:\n")
        if key == SECRET:
            func()
        else:
            print("The key is incorrect, try again next time")
    return wrapper

@check_user
def important_action():
    print("doing some important stuff")

@check_user
def another_important_action():
    important_action()

important_action()