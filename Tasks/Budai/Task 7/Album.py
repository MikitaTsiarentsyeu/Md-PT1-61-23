class Album:
    def __init__(self, title, artist, year, genre):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre