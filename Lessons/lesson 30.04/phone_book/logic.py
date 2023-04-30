import os
import csv
# repo = {'contact name':["4568468468", "4584325485"]}

class ContactsDB:

    __index = "index.txt"
    __numbers = "numbers.csv"

    def __init__(self) -> None:
        with open(ContactsDB.__index, 'a+'): pass
        with open(ContactsDB.__numbers, 'a+'): pass

    def get_all_records(self):
        c_list = []
        with open(ContactsDB.__index, 'r') as index:
            for i in index:
                c_list.append(Contact(i.strip()))

        with open(ContactsDB.__numbers, 'r') as numbers:
            reader = csv.reader(numbers)
            count = 0
            for c_number in reader:
                c_list[count].add_numbers(*c_number)
                count += 1

        return c_list

class ContactsManager:

    __db = ContactsDB()

    def get_all_records():
        records = ContactsManager.__db.get_all_records()
        return '\n'.join([str(x) for x in records])

    def get_record_by_name(name):
        pass

    def check_name(name):
        pass

    def add_record(name, numbers):
        pass


class Contact:

    def __init__(self, name, numbers=None):
        self.name = name
        if isinstance(numbers, list):
            self.__numbers = numbers
        else:
            self.__numbers = list()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def add_number(self, number):
        if number not in self.__numbers:
            self.__numbers.append(number)

    def add_numbers(self, *numbers):
        for number in numbers:
            self.add_number(number)

    def remove_number(self, number):
        if number in self.__numbers:
            self.__numbers.remove(number)

    def remove_numbers(self, *numbers):
        for number in numbers:
            self.remove_number(number)

    name = property(get_name, set_name)

    def __str__(self):
        return f"{self.name}:{','.join(self.__numbers)}"

def get_all_records():
    return ContactsManager.get_all_records()

def get_record_by_name(name):
    return ContactsManager.get_record_by_name(name)

def check_name(name):
    return ContactsManager.check_name(name)

def add_record(name, numbers):
    return ContactsManager.add_record(name, numbers)


if __name__ == "__main__":
    print(get_all_records())
    