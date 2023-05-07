import oop_logic

def add_new_movie():       
    elem = input("Enter title, director, year, genre separated by commas:\n")
    elem = list(elem.title().split(","))
    oop_logic.MovieManager.add_new_movie(*elem)    
    print("Your movie has been added!")

def get_list():             
    a = (oop_logic.MovieDB.get_list()) 
    print(a)
    
def search(gener):         
    try:
        word = input("Enter search value\n").title()
        while True:
            count = 0
            for i in gener:
                if i == word:
                    print(next(gener))
                    count += 1
            else:
                next(gener)
                count += 0
    except StopIteration:
        print("")
    if count == 0:
        print("Nothing found!")
    
def main_cycle():
    while True:
        answ = input('''Choose the main menu option:
                        0. Exit.
                        1. Add new movie.
                        2. Get list all movies.
                        3. Search for a movie by title / director / year / genre.
                        your choice: ''').strip()
        if answ == "0":
            print("Good bye!")
            break
        elif answ == "1":
            add_new_movie()
        elif answ == "2":
            get_list()
        elif answ == "3":
            answ2 = input('''Choose the search menu option:
                            1. Search by title.
                            2. Search by director.
                            3. Search by year.
                            4. Search by genre.
                            your choice: ''').strip()
            if answ2 == "1":
                search(oop_logic.MovieManager.search_by_title())
            elif answ2 == "2":
                search(oop_logic.MovieManager.search_by_director())
            elif answ2 == "3":
                search(oop_logic.MovieManager.search_by_year())
            elif answ2 == "4":
                search(oop_logic.MovieManager.search_by_genre())
            else:
                print("Choose a number from the list")
                continue
        else:
            print("Choose a number from the list")
            continue

if __name__== "__main__":
    main_cycle()