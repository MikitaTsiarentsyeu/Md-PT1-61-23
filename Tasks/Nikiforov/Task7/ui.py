import logic 

def add_movie(): 
    movie = []
    while True:
        while True:
            title = input("Enter the title of movie:\n")
            if len(title) == 0:
                print("This field is required and cannot be empty, try again")
                continue
            else:
                movie.append(title.title().strip())
            break
        while True:
            director = input("Enter the director of movie:\n")
            if len(director) == 0:
                print("This field is required and cannot be empty, try again")
                continue
            else:
                movie.append(director.title().strip())
            break
        while True:
            year = input("Enter the year the movie was released:\n").strip()
            if year.isdigit():
                year = int(year)
                if year < 1895:
                    print("The first movie was made in 1895, I guess you put the wrong date, try again")
                    continue
                elif year > 2023:
                    print("It's great that you can see the future, but let's talk about already existing movies")
                    continue
                else:
                    movie.append(str(year))
            else:
                print("This field can only contain numbers, try again")
                continue
            break
        while True:
            genre = input("Enter the genre of the movie:\n")
            if len(genre) == 0:
                print("This field is required and cannot be empty, try again")
                continue
            else:
                movie.append(genre.lower())
            break
        break
    logic.file_write(movie)
    print("The movie was added succesfully!")

def get_all():
    print("All movies in the collection:\n\n" + '\n'.join([f"{movie[0]}: {movie[2]} {movie[3].rstrip()} film directed by {movie[1]}" for movie in logic.list_collection()]))

def search_film():
    search_method = input("""
            1. Search by title.
            2. Search by director
            3. Search by year
            4. Search by genre
            5. Quit
            """)
    if search_method == '1':
        for i in logic.search_title():
            print(i)
    elif search_method == '2':
        for i in logic.search_director():
            print(i)
    elif search_method == '3':
        for i in logic.search_year():
            print(i)
    elif search_method == '4':
        for i in logic.search_genre():
            print(i)
    else:
        pass

    

def main_cycle():
    while True:
            answ = input("""
            Choose the menu option:
            1. Add a new movie to the collection
            2. List all movies in the collection
            3. Find a movie.
            4. Quit
            """)
            if answ == '1':
                add_movie()
            elif answ == '2':
                get_all()
            elif answ == '3':
                search_film()
            elif answ == '4':
                print('bye')
                break
            else:
                print("Choose a number from the list")
                continue
