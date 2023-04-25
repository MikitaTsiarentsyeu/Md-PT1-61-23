from logic import Collection

def main():
    collection = Collection()
    while True:
        print('1. Add a new album or movie to the collection.')
        print('2. List all albums or movies in the collection.')
        print('3. Search for an album or movie.')
        print('4. Quit the program.')
        choice = input('Enter your choice: ')
        if choice == '1':
            title = input('Enter the title: ')
            artist_director = input('Enter the artist or director: ')
            year = int(input('Enter the year: '))
            genre = input('Enter the genre: ')
            collection.add_item({
                'title': title,
                'artist_director': artist_director,
                'year': year,
                'genre': genre
            })
        elif choice == '2':
            collection.list_items()
        elif choice == '3':
            print('1. Search by title.')
            print('2. Search by artist/director.')
            print('3. Search by year.')
            print('4. Search by genre.')
            search_choice = input('Enter your choice: ')
            if search_choice == '1':
                title = input('Enter the title: ')
                for item in collection.search_title(title):
                    print(item)
            elif search_choice == '2':
                artist_director = input('Enter the artist or director: ')
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
            break


if __name__ == '__main__':
    main()
