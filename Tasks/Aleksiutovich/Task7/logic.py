import ijson
import json
# модуль ijson для работы с большими JSON-файлами.
# Он поможет считывать файл последовательно, экономя память.


class Collection:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.file_manager = FileManager(self.__file_path)
        self.items = self.file_manager.read_all_items()

    def get_file_path(self):
        return self.__file_path

    # def set_file_path(self, file):
    #     self.__file_path = file

    file_path = property(get_file_path) #, set_file_path)

    def __str__(self):
        return f"File collection is {self.file_path}"

    def add_item(self, item):
        # метод, который добавляет элемент в коллекцию.
        self.items.append(item)
        self.file_manager.write_all_items(self.items)

    def list_items(self):
        # метод, который выводит все элементы коллекции.
        for item in self.items:
            print(f"Title: {item['title']}, Director: {item['director']}, "
                  f"Year: {item['year']}, Genre: {item['genre']}")

    def edit_collection(self, item_index, key, val):
        # метод, который изменяет элемент коллекции.
        if key in item_index:
            item_index[key] = val
            self.file_manager.write_all_items(self.items)

    # Далее методы, которые ищут элементы коллекции.

    def search_title(self, title):
        return Searcher(self.items).search_by_title(title)

    def search_director(self, director):
        return Searcher(self.items).search_by_director(director)

    def search_year(self, year):
        return Searcher(self.items).search_by_year(year)

    def search_genre(self, genre):
        return Searcher(self.items).search_by_genre(genre)


class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.__file_path

    def set_file_path(self, file):
         self.__file_path = file

    file_path = property(get_file_path, set_file_path)

    def read_all_items(self):
        #метод, который читает все элементы из файла.
        try:
            with open(self.file_path, 'rb') as f:
                items = ijson.items(f, 'item')
                # print(list(items))
                return list(items)
        except FileNotFoundError:
            return []

    def write_all_items(self, items):
        # метод, который записывает все элементы в файл.
        with open(self.file_path, 'w') as f:
            json.dump(items, f)


class Searcher:
    def __init__(self, items):
        self.items = items

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    #items = property(get_items, set_items)

    def search_by_title(self, title):
        # метод, который ищет элементы по названию.
        for item in self.items:
            if item['title'] == title:
                yield item

        # return (item for item in self.items if item['title'] == title)

    def search_by_director(self, director):
        # метод, который ищет элементы по режиссеру.
        return (item for item in self.items if item['director'] == director)

    def search_by_year(self, year):
        # метод, который ищет элементы по году выпуска.
        return (item for item in self.items if item['year'] == year)

    def search_by_genre(self, genre):
        # метод, который ищет элементы по жанру.
        return (item for item in self.items if item['genre'] == genre)


if __name__ == '__main__':
# test
    # collection = Collection('df.json')
    # collection.add_item({'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972, 'genre': 'Crime'})
    # collection.list_items()
    # collection.items
    # result = collection.search_title('The Godfather')
    # print(result)

