import task_7_version_2_back


def add_album():
    album = ask_for_album()
    task_7_version_2_back.AlbumManager.add_album(album)


def show_all_albums():
    albums = task_7_version_2_back.AlbumManager.get_all_albums()
    for album in albums:
        print_album(album)


def ask_for_album():
    title = input('Enter the title: ')
    artist = input('Enter the artist: ')
    year = input_year('Enter the year: ')
    genre = input('Enter the genre: ')
    album = task_7_version_2_back.Album(title, artist, year, genre)
    return album


def print_album(album):
    print(f"""
        title - {album['title']}, 
        artist - {album['artist']}, 
        year - {album['year']}, 
        genre - {album['genre']}""")


def input_year(message):
    while True:
        try:
            n = int(input(message))
            if 0 < n < 2024:
                return n
            else:
                print('Incorrect year')
                continue
        except ValueError:
            print('Enter an integer')


print("This list is empty, you must first add to its information!")


def my_super_programm():
    while True:
        option = input("""
Please press number 2 and add to the list:

            0. Exit
            1. List all movies or songs
            2. Add a new movie or songs
            3. Find movie or song. 
            """).strip()
        if option == '0':
            break
        elif option == '1':
            show_all_albums()
        elif option == '2':
            add_album()
        elif option == '3':
            search_option = input("""
                            Choose option:
                            0. Exit
                            1. Search by title
                            2. Search by artist
                            3. Search by year
                            4. Search by genre
                        """).strip()
            if search_option == '0':
                break
            elif search_option == '1':
                title = input('Enter the title: ')
                for album in task_7_version_2_back.AlbumManager.search_title(title):
                    print_album(album)
            elif search_option == '2':
                artist = input('Enter the artist: ')
                for album in task_7_version_2_back.AlbumManager.search_artist(artist):
                    print_album(album)
            elif search_option == '3':
                year = input_year('Enter the year: ')
                for album in task_7_version_2_back.AlbumManager.search_year(year):
                    print_album(album)
            elif search_option == '4':
                genre = input('Enter the genre: ')
                for album in task_7_version_2_back.AlbumManager.search_genre(genre):
                    print_album(album)
            else:
                print('Choose the option from the list')
                continue
        else:
            print('Choose the option from the list')
            continue
