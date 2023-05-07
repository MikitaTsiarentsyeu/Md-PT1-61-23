import json

class MovieDB:                  
    __file = "movies.json"

    def get_list():
        with open(MovieDB.__file, "r") as database:
            for i in database:
                return i

class Movie:                      
    def __init__(self,title,director,year,genre):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre
        self.__movie = list()
    def get_title(self):
        return self.__title
    def get_director(self):
        return self.__director
    def get_year(self):
        return self.__year
    def get_genre(self):
        return self.__genre
    def add_movie(self, title):
        if title not in self.__movie:
            self.__movie.append({'title':self.title, 'director':self.director, 'year':self.year, 'genre':self.genre})
    def get_movie(self):
        for i in self.__movie:
            return i

    title = property(get_title)
    director = property(get_director)
    year = property(get_year)
    genre = property(get_genre)
    movie = property(get_movie)


class MovieManager:
   
    def add_new_movie(title,director,year,genre):
        new_movie = Movie(title,director,year,genre)
        new_movie.add_movie(title)
        with open("movies.json", "r") as f:
            d = json.load(f)
            d.append(Movie.get_movie(new_movie))
        with open("movies.json", "w") as f:
            json.dump(d,f)  

    def search_by_title():
        with open("movies.json", "r") as f:
            film = json.load(f)
            for i in film: 
                yield i["title"]
                yield i

    def search_by_director():
        with open("movies.json", "r") as f:
            film = json.load(f)
            for i in film: 
                yield i["director"]
                yield i

    def search_by_year():
        with open("movies.json", "r") as f:
            film = json.load(f)
            for i in film: 
                yield i["year"]
                yield i

    def search_by_genre():
        with open("movies.json", "r") as f:
            film = json.load(f)
            for i in film: 
                yield i["genre"]
                yield i

    