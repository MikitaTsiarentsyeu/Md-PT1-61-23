import json


class DataBase:
    """Storage and reading if the entire collection of films"""

    def get_all_movies():
        """Output of the entire collection of films"""
        result = ""
        with open("movie_collection.json", "r") as file:
            data = json.load(file)       
        for i in data:
            result += f"Movie title: {i['title']}, film director: {i['director']}, release year: {i['year']}, film genre: {i['genre']}\n"
        return result.strip()


class Movie:
    """Movie description class"""

    def __init__(self, title, director, year, genre):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre
        self.__data = list()

    def get_title(self):
        return self.__title

    def get_director(self):
        return self.__director

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def add_movie(self, title):
        if title not in self.__data:
            self.__data.append(
                {'title': self.__title, 'director': self.__director,
                 'year': self.__year, 'genre': self.__genre}
            )

    def get_movie(self):
        for movie in self.__data:
            return movie

    title = property(get_title)
    director = property(get_director)
    year = property(get_year)
    genre = property(get_genre)
    movie = property(get_movie)


class MovieManager:
    """Class for adding and searching for movies in the collection"""

    def add_new_movie(title, director, year, genre):
        """Adding a new movie to the collection"""
        new_movie = Movie(title, director, year, genre)
        new_movie.add_movie(title)
        with open("movie_collection.json", "r") as file:
            data = json.load(file)
            data.append(Movie.get_movie(new_movie))
        with open("movie_collection.json", "w") as file:
            json.dump(data, file)

    def search():
        with open("movie_collection.json", "r") as file:
            movies = json.load(file)
            for movie in movies:
                yield movie                





