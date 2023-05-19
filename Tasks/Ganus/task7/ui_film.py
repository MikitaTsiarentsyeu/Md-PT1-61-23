
import film_logic
from pprint import pprint

def add_new_film_ui():
    
    title = ask_for_title()
    director = ask_for_director()
    year = ask_for_year()
    genre = ask_for_genre()
    films = film_logic.Film.add_new_film(title, director, year, genre)
    print("the film was added")

def get_all_films_ui():
    pprint(film_logic.FilmBD.get_all_films())

def search_film_by_title1():
    by_title = ask_for_title()
    for i in film_logic.ServiceData.search_film():
        for j in i:
            for key, valye in j.items():
                if key == "title":
                    if valye == by_title:
                        yield i
                        
def search_film_by_title():
    p = search_film_by_title1()
    count = 0
    while count < len(film_logic.ServiceData.search_film()):
        try:
            print(next(p))
            count += 1
        except StopIteration:
            return main_cycle()
    
def search_film_by_director1():
    by_director = ask_for_director()
    for i in film_logic.ServiceData.search_film():
        for j in i:
            for key, valye in j.items():
                if key == "director":
                    if valye == by_director:
                        yield i

def search_film_by_director():
    p = search_film_by_director1()
    count = 0
    while count < len(film_logic.ServiceData.search_film()):
        try:
            print(next(p))
            count += 1
        except StopIteration:
            return main_cycle()
    

def search_film_by_year1():
    by_year = ask_for_year()
    for i in film_logic.ServiceData.search_film():
        for j in i:
            for key, valye in j.items():
                if key == "year":
                    if valye == by_year:
                        yield i

def search_film_by_year():
    p = search_film_by_year1()
    count = 0
    while count < len(film_logic.ServiceData.search_film()):
        try:
            print(next(p))
            count += 1
        except StopIteration:
            return main_cycle()

def search_film_by_genre1():
    by_genre = ask_for_genre()
    
    for i in film_logic.ServiceData.search_film():
        for j in i:
            for key, valye in j.items():
                if key == "genre":
                    if by_genre in ",".join(valye):
                        yield i
                        

def search_film_by_genre():
    p = search_film_by_genre1()
    count = 0
    while count < len(film_logic.ServiceData.search_film()):
        try:
            print(next(p))
            count += 1
        except StopIteration:
            return main_cycle()
    


def ask_for_title():
    title = ""
    while not title:
        return input(f"please, enter the title:\n")
    return title

def ask_for_director():
    director = ""
    while not director:
        return input(f"please, enter the director:\n")
    return director

def ask_for_year():
    year = ""
    while not year:
        return input(f"please, enter the year:\n")
    return year

def ask_for_genre():
    genre = ""
    while not genre:
        return input(f"please, enter the genre:\n")
    return genre



def main_cycle():
    while True:
        answ = input("""
            Choose the menu option:
            0. Exit
            1. Add new film
            2. Get all films
            3. Search film:
                3.1 Search film by title
                3.2 Search film by director
                3.3 Search film by year
                3.4 Search film by genre

        """).strip()
        if answ == "0":
            break
        elif answ == "1":
            add_new_film_ui()
        elif answ == "2":
            get_all_films_ui()
        elif answ == "3":
            print("Choose a number from the list of searched films")
            continue
        elif answ == "3.1":
            search_film_by_title()
        elif answ == "3.2":
            search_film_by_director()
        elif answ == "3.3":
            search_film_by_year()
        elif answ == "3.4":
            search_film_by_genre()
        else:
            print("Choose a number from the list")
            continue

