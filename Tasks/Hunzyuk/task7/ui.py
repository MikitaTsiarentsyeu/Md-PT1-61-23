import logic

def get_all_movies_collection():
    responce = (logic.DataBase.get_all_movies())
    print(responce)
    

def add_new_movie():       
    params = input("Enter title, director, year, genre:\n")
    params = list(params.title().split(","))
    logic.MovieManager.add_new_movie(*params)    
    print("The movie has been successfully added to the collection!")


def search_title():
    result = ""
    try:
        title = input("Enter movie title\n").strip()
        responce = logic.MovieManager.search()
        for i in responce:
            if title.lower() == i['title'].lower():
                result += f"Movie title: {i['title']}, film director: {i['director']}, release year: {i['year']}, film genre: {i['genre']}\n"
        print(result.strip())
            
    except KeyError:
        print("This movie is not in the collection")

def search_director():
    result = "" 
    try:
        director = input("Enter director's name\n").strip()
        responce = logic.MovieManager.search()
        for i in responce:
            if director.lower() == i['director'].lower():
                result += f"Movie title: {i['title']},release year: {i['year']}, film genre: {i['genre']}\n"
        print(result.strip())
    except KeyError:
        print("There is no director with this name in database")


def search_year():
    result = ""
    try:
        year = input("Enter year\n").strip()
        responce = logic.MovieManager.search()
        for i in responce:
            if year == i['year']:
                result += f"Movie title: {i['title']}, film director: {i['director']}, film genre: {i['genre']}\n"
        print(result.strip())
    except ValueError:
        print("There are no films of this year if release in the collection")

def search_genre():
    result = ""
    try:
        genre = input("Enter genre\n").strip()
        responce = logic.MovieManager.search()
        for i in responce:
            if genre.lower() == i['genre'].lower():
                result += f"Movie title: {i['title']}, film director: {i['director']}, release year: {i['year']}\n"
        print(result.strip())
    except:
        print("There are no films of this genre in the collection")


def main_cicle():
  
    while True:
        answ = input("""
            Choose the menu option:
            0. Exit
            1. Get a list of all movies
            2. Add a new movies to the collection
            3. Movie title search
            4. Search movie by director
            5. Search movie by release year
            6. Search movie by genre
        """).strip()

        if answ == '0':
            break
        elif answ == '1':
            get_all_movies_collection()
        elif answ == '2':
            add_new_movie()
        elif answ == '3':
            search_title()
        elif answ == '4':
            search_director()
        elif answ == '5':
            search_year()
        elif answ == '6':
            search_genre()
        else:
            print("Choose a number from the list")