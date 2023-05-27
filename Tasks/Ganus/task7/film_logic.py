import json
from pprint import pprint
data = {}
data["film"] = []

class FilmBD:
    __film = "data_file.json"
    def get_all_films():
        with open("data_file.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    
        


class Film:
    def __init__(self, title, director, year, genre = []):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title
    def get_director(self):
        return self.__director
    def set_director(self, director):
        self.__director = director
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year  
    def get_genre(self):
        return self.__genre
    def set_genre(self, genre):
        self.__genre = genre  
    title = property(get_title, set_title)
    director = property(get_director, set_director)
    year = property(get_year, set_year)
    genre = property(get_genre, set_genre)
    def add_new_film(title, director, year, genre):
        data["film"].append([
            {"title":title},
            {"director":director},
            {"year":year},
            {"genre":[genre]}
        ])
        with open ("data_file.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file)
            write_file.write("\n")


class ServiceData:

    def search_film():
        new_dict = []
        with open("data_file.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            for valye in data["film"]:
                new_dict += [valye]
            return new_dict
        
            

       


