import time
from logic import Collection



def main():
    collection = Collection()
    message = """MovieShelf is a movie library program that allows users 
to easily browse and add movies to their collection. With its 
intuitive interface and powerful search capabilities, MovieShelf 
makes it easy to keep track of your favorite films."""
    print(message)
    time.sleep(2)
    while True:
        print('                  Menu                        ')
        print('1. Add a new album or movie to the collection.')
        print('2. List all albums or movies in the collection.')
        print('3. Search for an album or movie.')
        print('4. Edit movie entry.')
        print('5. Quit the program.')
        print('6. Help')
        choice = input('Enter your choice: ')
        if choice == '1':
            title = input('Enter the title: ')
            director = input('Enter the director: ')
            year = int(input('Enter the year: '))
            genre = input('Enter the genre: ')
            collection.add_item({
                'title': title,
                'director': director,
                'year': year,
                'genre': genre
            })
        elif choice == '2':
            collection.list_items()
        elif choice == '3':
            print('1. Search by title.')
            print('2. Search by director.')
            print('3. Search by year.')
            print('4. Search by genre.')
            search_choice = input('Enter your choice: ')
            if search_choice == '1':
                title = input('Enter the title: ')
                for item in collection.search_title(title):
                    print(item)
            elif search_choice == '2':
                artist_director = input('Enter the director: ')
                for item in collection.search_artist_director(artist_director):
                    print(item)
            elif search_choice == '3':
                year = int(input('Enter the year: '))
                for item in collection.search_year(year):
                    print(item)
            elif search_choice == '4':
                genre = input('Enter the genre: ')
                for item in collection.search_genre(genre):
                    print(item)

        elif choice == '4':
            print("Enter the title of the movie you want to change information about")
            title = input('Enter the title: ')
            for item in collection.search_title(title):
                print(item)
                x = input("What do you need to update? ")
                new_val = input("Enter the new value: ")
                if x in item:
                    item[x] = new_val
                print(item)
                collection.save_to_file()

        elif choice == '5':
            break

        elif choice == '6':
            print('You need to enter the number corresponding '
                  'to the menu bar.')

        else:
            print('You have entered an incorrect query try '
                  'to enter it again')
            continue


if __name__ == '__main__':
    main()
