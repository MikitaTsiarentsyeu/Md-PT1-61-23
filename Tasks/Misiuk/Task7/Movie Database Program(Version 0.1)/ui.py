import logic


def add_film():
    title = input('Enter the name of the movie:\n')
    producer = input('Enter the film director:\n')
    year = input('Enter the year of the movie:\n')
    genre = input('Enter the movie genre:\n')
    
    print(logic.add_new_record(title,producer,year,genre))
    

def get_all_record():
    print(logic.get_all_records())
    

def search_title():
    title = input('Enter a title to search for:\n')
    logic.search_title(title)
    
def search_director():
    director = input('Enter a director to search for:\n')
    logic.search_director(director)
    
def search_year():
    year = input('Enter a year to search for:\n')
    logic.search_year(year)
    
def search_genre():
    genre = input('Enter a genre to search for:\n')
    logic.search_genre(genre)

def ui_interface():
    while True:
        choice = input("""
        Select the desired item in the menu:
        0.Exit
        1.Get all records
        2.Search record
        3.Add new record
        """).strip()
        if choice == '0':
            break
        elif choice == '1':
            get_all_record()
        elif choice == '2':
            next_choice = input("""
            Find an entry by:
            0.Exit
            1.Title
            2.Director
            3.Years
            4.Genre
            """)
            if next_choice == '0':
                break
            elif next_choice == '1':
                search_title()
            elif next_choice == '2':
                search_director()
            elif next_choice == '3':
                search_year()
            elif next_choice == '4':
                search_genre()
            else:
                print('Select a number from from the menu') 
        elif choice == '3':
            add_film()
        else:
            print('Select a number from from the menu')
        
        
        
        
ui_interface()