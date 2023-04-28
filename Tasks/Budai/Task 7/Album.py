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
