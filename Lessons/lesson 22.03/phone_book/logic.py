repo = {'contact name':["4568468468", "4584325485"]}

def get_all_records():
    return '\n'.join([f"{name}:{','.join(numbers)}" for name, numbers in repo.items()])

def get_record_by_name(name):
    try:
        numbers = repo[name]
        return f"{name}:{','.join(numbers)}"
    except KeyError:
        return ""

def check_name(name):
    return name in repo

def add_record(name, numbers):
    repo[name] = numbers


if __name__ == "__main__":
    print(get_all_records())