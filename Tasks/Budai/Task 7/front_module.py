import back_module
from Album import Album


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


def print_album(album):
    print(f"""
            Title - {album['title']}, 
            artist - {album['artist']}, 
            year - {album['year']}, 
            genre - {album['genre']}""")


def add_album():
    album = ask_for_album()
    back_module.add_album(album)


def show_all_albums():
    albums = back_module.get_all_albums()
    for album in albums:
        print_album(album)


def ask_for_album():
    title = input('Enter the title: ')
    artist = input('Enter the artist: ')
    year = input_year('Enter the year: ')
    genre = input('Enter the genre: ')
    album = Album(title, artist, year, genre)
    return album


def main_cycle():
    while True:
        option = input("""
                Choose the menu option:
                0. Exit
                1. List all albums
                2. Add new album
                3. Search for album
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
                for album in back_module.search_title(title):
                    print_album(album)
            elif search_option == '2':
                artist = input('Enter the artist: ')
                for album in back_module.search_artist(artist):
                    print_album(album)
            elif search_option == '3':
                year = input_year('Enter the year: ')
                for album in back_module.search_year(year):
                    print_album(album)
            elif search_option == '4':
                genre = input('Enter the genre: ')
                for album in back_module.search_genre(genre):
                    print_album(album)
            else:
                print('Choose the option from the list')
                continue
        else:
            print('Choose the option from the list')
            continue



