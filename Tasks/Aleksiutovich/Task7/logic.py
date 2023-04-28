import json




class Collection:
    def __init__(self):
        self.items = []
        self.load_from_file()

    def add_item(self, item):
        self.items.append(item)
        self.save_to_file()

    def list_items(self):
        for item in self.items:
            for key, val in item.items():
                print(f' {key} - {val} |', end=' ')
            print(' ')

    #You need write this function
    def edit_collection(self): pass

    def search_title(self, title):
        for item in self.items:
            if item['title'] == title:
                yield item

    def director(self, director):
        for item in self.items:
            if item['director'] == director:
                yield item

    def search_year(self, year):
        for item in self.items:
            if item['year'] == year:
                yield item

    def search_genre(self, genre):
        for item in self.items:
            if item['genre'] == genre:
                yield item

    def save_to_file(self):
        with open('df.json', 'w') as f:
            json.dump(self.items, f)

    def load_from_file(self):
        try:
            with open('df.json', 'r') as f:
                self.items = json.load(f)
        except FileNotFoundError:
            pass



if __name__ == '__main__':
    col = Collection
    print(type(col))
    import inspect

    c = inspect.getmembers(col, predicate=inspect.ismethod)
    print(type(c))


