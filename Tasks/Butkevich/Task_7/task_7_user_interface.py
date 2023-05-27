import task_7_logic

print("This list is empty, you must first add to its information!")


def my_super_programm():
    while True:
        menu = input("""
Please press number 1 and add to the list:

            1. Add a new movie or songs
            2. List all movies or songs
            3. Find movie or song.
            4. Exit
            """)
        if menu == '1':
            add_movie()
        elif menu == '2':
            get_all()
        elif menu == '3':
            search_film()
        elif menu == '4':
            print('List formed,you have left the programm')
            break
        else:
            print("Choose a number from the list")
            continue


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
                if year < 1800:
                    print("At that time there was no movie, choose a year more")
                    continue
                elif year > 2024:
                    print("You have to choose a smaller year, this year has not yet")
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
    task_7_logic.file_write(movie)
    print("The movie or song was added succesfully!")


def get_all():
    print("All movies in the collection:\n\n" + '\n'.join(
        [f"{movie[0]}: {movie[2]} {movie[3].rstrip()} film directed by {movie[1]}" for movie in
         task_7_logic.list_collection()]))


def search_film():
    search_method = input("""
            1. Search by title.
            2. Search by director
            3. Search by year
            4. Search by genre
            5. Quit
            """)
    if search_method == '1':
        for i in task_7_logic.search_title():
            print(i)
    elif search_method == '2':
        for i in task_7_logic.search_director():
            print(i)
    elif search_method == '3':
        for i in task_7_logic.search_year():
            print(i)
    elif search_method == '4':
        for i in task_7_logic.search_genre():
            print(i)
    else:
        pass
