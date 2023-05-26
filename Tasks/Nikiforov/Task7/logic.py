import csv

class MovieDB:

    def get_all(): 
        with open('Tasks/Nikiforov/Task7/list_of_movies.csv', 'r') as f:
            reader = csv.reader(f)
            list_of_movies = [row for row in reader]
            return list_of_movies
            
class Movie:

    def __init__(self,title,director,year,genre):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title
    def get_director(self):
        return self.__director
    def get_year(self):
        return self.__year
    def get_genre(self):
        return self.__genre
    def get_movie(self):
        return [self.__title,self.__director,self.__year,self.__genre]

    title = property(get_title)
    director = property(get_director)
    year = property(get_year)
    genre = property(get_genre)
    movie = property(get_movie)

class MovieManager:

    __file = 'Tasks/Nikiforov/Task7/list_of_movies.csv'
    __db = MovieDB.get_all()

    def add_movie(title,director,year,genre):
        with open(MovieManager.__file, 'a+', newline='') as f:
            writer = csv.writer(f)
            if MovieManager.check_movie(title):
                return 'This movie is already in the collection'
            new_movie = Movie(title,director,year,genre)
            writer.writerow(new_movie.movie)
            return 'The movie was added succesfully!'                
            
    def check_movie(title):
        for movie in MovieManager.__db:
            if movie[0] == title:
                return True
        return False
    
    def search_title(title):
        for movie in MovieManager.__db:
            if movie[0] == title:
                return ' '.join(movie)
            
    def search_director(director):
        for movie in MovieManager.__db:
            if movie[1] == director:
                yield ' '.join(movie)

    def search_year(year):
        for movie in MovieManager.__db:
            if movie[2] == year:
                yield ' '.join(movie)

    def search_genre(genre):
        for movie in MovieManager.__db:
            if movie[3] == genre:
                yield ' '.join(movie)
