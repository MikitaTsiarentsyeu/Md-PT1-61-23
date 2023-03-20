# -*- coding: utf-8 -*-
import datetime as dt

'''without checking for the correctness of the input'''


# Implement a text output of the time entered from the console (the user should input data in the format hh:mm).
#
# Show the responses to the user in Russian according to the rules listed below:
class СonvertingTime:
    def __init__(self):
        self.dictionary_1 = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре", 5: "Пять", 6: "Шесть", 7: "Семь",
                             8: "Восемь", 9: "Девять", 10: "Десять", 11: "Одинадцать", 12: "Двенадцать"}
        self.dictionary_2 = {1: "первого", 2: "второго", 3: "третьего", 4: "четвертого", 5: "пятого", 6: "шестого",
                             7: "седьмого", 8: "восьмого", 9: "девятого", 10: "десятого", 11: "одинадцатого",
                             12: "двенадцатого", 13: "первого"}
        self.dictionary_3 = {1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
                             7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать",
                             12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
                             16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать",
                             20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят", 0: ""}
        self.dictionary_4 = {15: "пятнадцати", 14: "четырнадцати", 13: "тринадцати", 12: "двенадцати",
                             11: "одинадцати", 10: "десяти", 9: "девяти", 8: "восьми", 7: "семи",
                             6: "шести", 5: "пяти", 4: "четырех", 3: "трех", 2: "двух", 1: "одной"}
        self.list = (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44)
        self.list_2 = (1, 21, 31, 41)
        self.list_3 = (2, 3, 4, 14, 15, 16)
        self.list_4 = (11, 12, 13, 14, 15, 16, 17, 18, 19)

    def input_time_find_hour_and_minute(self):
        self.digital_time_input = str(input("Введите время в формате hh:mm.\n Пример, 16:00 \n \t")).strip()
        # self.digital_time_input = "12:58"
        self.data_time = dt.datetime.strptime(self.digital_time_input, "%H:%M")
        self.hour = int(self.data_time.hour)
        self.minute = int(self.data_time.minute)

    def modul_1(self):
        if self.hour > 12:
            if self.minute in self.list_2:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute - self.minute % 10]} "
                      f"{self.dictionary_3[self.minute % 10]} "
                      f"минута {self.dictionary_2[self.hour + 1 - 12]}")
            elif self.minute in self.list_4:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute]} "
                      f"минут {self.dictionary_2[self.hour + 1 - 12]}")
            elif self.minute in self.list:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute - self.minute % 10]} "
                      f"{self.dictionary_3[self.minute % 10]} "
                      f"минуты {self.dictionary_2[self.hour + 1 - 12]}")
            else:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute - self.minute % 10]} "
                      f"{self.dictionary_3[self.minute % 10]} "
                      f"минут {self.dictionary_2[self.hour + 1 - 12]}")
        else:
            if self.minute in self.list_2:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute - self.minute % 10]} "
                      f"{self.dictionary_3[self.minute % 10]} "
                      f"минута {self.dictionary_2[self.hour + 1]}")
            elif self.minute in self.list_4:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute]} "
                      f"минут {self.dictionary_2[self.hour + 1]}")
            elif self.minute in self.list:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute - self.minute % 10]} "
                      f"{self.dictionary_3[self.minute % 10]} "
                      f"минуты {self.dictionary_2[self.hour + 1]}")
            else:
                print(f"{self.digital_time_input} - {self.dictionary_3[self.minute - self.minute % 10]} "
                      f"{self.dictionary_3[self.minute % 10]} "
                      f"минут {self.dictionary_2[self.hour + 1]}")

    def modul_2(self):
        if self.hour == 1 or self.hour == 13:
            if self.hour > 12:
                print(f"{self.digital_time_input} - "
                      f"{self.dictionary_1[self.hour - 12].lower()} час ровно")
            else:
                print(f"{self.digital_time_input} - "
                      f"{self.dictionary_1[self.hour].lower()} час ровно")
        elif self.hour in self.list_3:
            if self.hour > 12:
                print(f"{self.digital_time_input} - "
                      f"{self.dictionary_1[self.hour - 12].lower()} часа ровно")
            else:
                print(f"{self.digital_time_input} - "
                      f"{self.dictionary_1[self.hour].lower()} часа ровно")
        else:
            if self.hour > 13:
                print(f"{self.digital_time_input} - "
                      f"{self.dictionary_1[self.hour - 12].lower()} часов ровно")
            else:
                print(f"{self.digital_time_input} - "
                      f"{self.dictionary_1[self.hour].lower()} часов ровно")

    def modul_3(self):
        if self.hour > 12:
            if self.minute == 59:
                print(
                    f"{self.digital_time_input} - без {self.dictionary_4[60 - self.minute]} "
                    f"минуты {self.dictionary_2[self.hour + 1 - 12]}")
            else:
                print(
                    f"{self.digital_time_input} - без {self.dictionary_4[60 - self.minute]} "
                    f"минут {self.dictionary_2[self.hour + 1 - 12]}")
        else:
            if self.minute == 59:
                print(
                    f"{self.digital_time_input} - без {self.dictionary_4[60 - self.minute]} "
                    f"минуты {self.dictionary_2[self.hour + 1]}")
            else:
                print(
                    f"{self.digital_time_input} - без {self.dictionary_4[60 - self.minute]} "
                    f"минут {self.dictionary_2[self.hour + 1]}")
            # print(
            #     f"{self.digital_time_input} - без {self.dictionary_4[60 - self.minute]} "
            #     f"минут {self.dictionary_2[self.hour + 1]}")

    def logic_of_actions(self):
        self.input_time_find_hour_and_minute()
        # min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
        if self.minute == 0:
            self.modul_2()
        # min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
        elif self.minute < 30:
            self.modul_1()
        # min == 30: половина такого-то (15:30 - половина четвёртого)
        elif self.minute == 30:
            if self.hour > 12:
                print(f"{self.digital_time_input} - половина {self.dictionary_2[self.hour + 1 - 12]}")
            else:
                print(f"{self.digital_time_input} - половина {self.dictionary_2[self.hour + 1]}")

        elif self.minute > 30 and self.minute < 45:
            self.modul_1()
        # min >= 45 без min такого-то (08:54 - без шести минут девять)
        elif self.minute >= 45:
            self.modul_3()
        else:
            print("Что-то пошло не так!")
            exit()

    def start(self):
        self.logic_of_actions()

def conver_time():
    x = СonvertingTime()
    try:
        x.start()
    except KeyError:
        print("00:00 - полночь")
    except ValueError:
        print("Ошибка")
        print("_______" * 4)
        print("Были введены некоректные данные")

conver_time()