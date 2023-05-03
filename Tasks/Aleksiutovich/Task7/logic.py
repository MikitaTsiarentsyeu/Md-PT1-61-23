import ijson
import json


class Collection:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_manager = FileManager(self.file_path)
        self.items = self.file_manager.read_all_items()

    def add_item(self, item):
        self.items.append(item)
        self.file_manager.write_all_items(self.items)

    def list_items(self):
        for item in self.items:
            for key, val in item.items():
                print(f' {key} - {val} |', end=' ')
            print(' ')

    def edit_collection(self, item_index, key, val):
        if key in item_index:
            item_index[key] = val
            self.file_manager.write_all_items(self.items)

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

    def read_all_items(self):
        try:
            with open(self.file_path, 'rb') as f:
                items = ijson.items(f, 'item')
                #print(list(items))
                return list(items)
        except FileNotFoundError:
            return []

    def write_all_items(self, items):
        with open(self.file_path, 'w') as f:
            json.dump(items, f)


class Searcher:
    def __init__(self, items):
        self.items = items

    def search_by_title(self, title):
        for item in self.items:
            if item['title'] == title:
                yield item

        # return (item for item in self.items if item['title'] == title)

    def search_by_director(self, director):
        return (item for item in self.items if item['director'] == director)

    def search_by_year(self, year):
        return (item for item in self.items if item['year'] == year)

    def search_by_genre(self, genre):
        return (item for item in self.items if item['genre'] == genre)


if __name__ == '__main__':
    #x = FileManager('df.json')

    collection = Collection('df.json')
    collection.add_item({'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972, 'genre': 'Crime'})
    collection.list_items()
    collection.items
    result = collection.search_title('The Godfather')
    print(result)
