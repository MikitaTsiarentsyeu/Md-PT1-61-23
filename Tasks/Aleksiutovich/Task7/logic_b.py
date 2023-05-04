import json
from abc import ABC, abstractmethod


# Этот код написан с помощью ChatGPT4.

class FilePath(ABC):
    @abstractmethod
    def save(self, items):
        pass

    @abstractmethod
    def load(self):
        pass


class JsonFilePath(FilePath):
    def __init__(self, path):
        self.path = path

    def save(self, items):
        with open(self.path, 'w') as f:
            json.dump(items, f)

    def load(self):
        try:
            with open(self.path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []


class Collection:
    def __init__(self, file_path):
        self.file_path = JsonFilePath(file_path)
        self.items = self.file_path.load()

    def add_item(self, item):
        self.items.append(item)
        self.file_path.save(self.items)

    def list_items(self):
        for item in self.items:
            for key, val in item.items():
                print(f' {key} - {val} |', end=' ')
            print(' ')

    def edit_collection(self, item_index, key, val):
        if key in item_index:
            item_index[key] = val
        self.file_path.save(self.items)

    def _search(self, key, value):
        for item in self.items:
            if item[key] == value:
                yield item

    def search_title(self, title):
        return self._search('title', title)

    def search_director(self, director):
        return self._search('director', director)

    def search_year(self, year):
        return self._search('year', year)

    def search_genre(self, genre):
        return self._search('genre', genre)


if __name__ == '__main__':
    # collection = Collection('df.json')
    # collection.add_item({'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972, 'genre': 'Crime'})
    # collection.list_items()
    # collection.edit_collection('The Godfather', 'year', 1974)
    # collection.items
    # result = collection.search_title('The Godfather')
    # print(result)
