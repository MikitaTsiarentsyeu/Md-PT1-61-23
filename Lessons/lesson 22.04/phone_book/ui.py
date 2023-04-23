import logic

def get_all_recodrs():
    print(logic.get_all_records())

def get_record_by_name():
    name = ask_for_name()
    res = logic.get_record_by_name(name)
    if res:
        print(res)
    else:
        print("nothing was found")

def add_new_record():
    name, check = check_name()
    while check:
        print("the name is already in use, choose another")
        name, check = check_name()
    numbers = ask_for_numbers()
    logic.add_record(name, numbers)
    print("the record was added")

def check_name():
    name = ask_for_name()
    check = logic.check_name(name)
    return name, check

def ask_for_param(param_name):
    return input(f"please enter the {param_name}:\n")

def ask_for_name():
    name = ""
    while not name:
        name = ask_for_param("name (it should not be empty)")
    return name

def ask_for_numbers():
    numbers = []
    while True:
        number = ask_for_param("a number or press enter when all are entered")
        if number:
            numbers.append(number)
            continue
        else:
            if len(numbers) > 0:
                break
            else:
                continue
    return numbers

def main_cycle():
    while True:
        answ = input("""
            Choose the menu option:
            0. Exit
            1. Get all records
            2. Get a record by name
            3. Add new record
        """).strip()
        if answ == '0':
            break
        elif answ == '1':
            get_all_recodrs()
        elif answ == '2':
            get_record_by_name()
        elif answ == '3':
            add_new_record()
        else:
            print("Choose a number from the list")
            continue
