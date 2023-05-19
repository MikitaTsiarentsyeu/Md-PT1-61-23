import json


class Album:
    def __init__(self, title, artist, year, genre):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    title = property(get_title)
    artist = property(get_artist)
    year = property(get_year)
    genre = property(get_genre)


class AlbumManager:
    @staticmethod
    def add_album(album):
        new_album = {'title': album.title,
                     'artist': album.artist,
                     'year': album.year,
                     'genre': album.genre}
        try:
            with open('albums.json', encoding='utf-8', mode='r') as file:
                data = json.load(file)
            data['albums'].append(new_album)
            with open('albums.json', encoding='utf-8', mode='w') as file1:
                json.dump(data, file1, ensure_ascii=False, indent=2)
        except FileNotFoundError:
            print('File not found')

    @staticmethod
    def get_all_albums():
        try:
            with open('albums.json', encoding='utf-8', mode='r') as file:
                data = json.load(file)
                return data['albums']
        except FileNotFoundError:
            print('File not found')

    @staticmethod
    def search_title(text):
        for album in AlbumManager.get_all_albums():
            if text.lower() in album['title'].lower():
                yield album

    @staticmethod
    def search_artist(text):
        for album in AlbumManager.get_all_albums():
            if text.lower() in album['artist'].lower():
                yield album

    @staticmethod
    def search_year(year):
        for album in AlbumManager.get_all_albums():
            if year == album['year']:
                yield album

    @staticmethod
    def search_genre(text):
        for album in AlbumManager.get_all_albums():
            if text.lower() in album['genre'].lower():
                yield album