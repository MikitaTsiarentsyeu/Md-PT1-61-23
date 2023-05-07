import csv


class Movie:
    
    def __init__(self,title,producer,year,genre):
        
        self.__title = title
        self.__producer = producer
        self.__year = year
        self.__genre = genre
        
    def get_title(self):
        return self.__title
    def get_producer(self):
        return self.__producer
    def get_year(self):
        return self.__year
    def get_genre(self):
        return self.__genre
    
        
    def set_title(self,title):
        self.__title = title
    def set_producer(self,producer):
        self.__producer = producer
    def set_year(self,year):
        self.__year = year
    def set_genre(self,genre):
        self.__genre = genre
    
        
    title = property(get_title,set_title)
    producer = property(get_producer,set_producer)
    year = property(get_year, set_year)
    genre = property(get_genre,set_genre)
    
    
    def __str__(self):
        return f"""
    Title: {self.__title}
    Director: {self.__producer}
    Year: {self.__year}
    Genre: {self.__genre}"""
    
    
    def __getstate__(self) -> list:
        state = []
        state.append(self.__title)
        state.append(self.__producer)
        state.append(self.__year)
        state.append(self.__genre)
        return state
    
    
class Collection:
    
    __collection = "collection.csv"
    
    
    def __init__(self):
        with open(Collection.__collection, 'a+'):
            pass
    
    
    def get_all_records(self):
        with open(Collection.__collection, 'r') as col_file:
            reader = csv.reader(col_file)
            for line in reader:
                result =  Movie(line[0],line[1],line[2],line[3])
                print(result)
        return '\nThe End.....'

    
    def add_new_record(title,producer,year,genre):
        count = 0
        with open(Collection.__collection, 'r') as read_file:
            reader = csv.reader(read_file)
            record = Movie(title,producer,year,genre)
            
            for line in reader:
                if line == record.__getstate__():
                    count = 1
                    print('\nThis entry is already in the database')
            if count == 0:
                with open(Collection.__collection, 'a',newline='\n') as col_file:
                    writer = csv.writer(col_file,delimiter=",")
                    writer.writerow(record.__getstate__())
                    return '\nThe database has been updated.....'
    
    
    def search_title(self,title):
        with open(Collection.__collection, 'r') as col_file:
            reader = csv.reader(col_file)
            for row in reader:
                if row[0] == title:
                    yield Movie(row[0],row[1],row[2],row[3])
                    
    def search_director(self,director):
        with open(Collection.__collection, 'r') as col_file:
            reader = csv.reader(col_file)
            for row in reader:
                if row[1] == director:
                    yield Movie(row[0],row[1],row[2],row[3])
                    
    def search_year(self,year):
        with open(Collection.__collection, 'r') as col_file:
            reader = csv.reader(col_file)
            for row in reader:
                if row[2] == year:
                    yield Movie(row[0],row[1],row[2],row[3])
                    
    def search_genre(self,genre):
        with open(Collection.__collection, 'r') as col_file:
            reader = csv.reader(col_file)
            for row in reader:
                if row[3] == genre:
                    yield Movie(row[0],row[1],row[2],row[3])
            
            
            
class Information_search:
    
    __cl = Collection()
    
    def get_all_records():
        records = Information_search.__cl.get_all_records()
        return records
  
    def search_title(title):
        records = Information_search.__cl.search_title(title)
        for line in records:
           print(line)
  
    def search_director(director):
        records = Information_search.__cl.search_director(director)
        for line in records:
            print(line)
            
    def search_year(year):
        records = Information_search.__cl.search_year(year)
        for line in records:
            print(line)
            
    def search_genre(genre):
        records = Information_search.__cl.search_genre(genre)
        for line in records:
            print(line)
            
            
            
def add_new_record(title,producer,year,genre):
    return Collection.add_new_record(title=title,producer=producer,year=year,genre=genre)          


def get_all_records():
    return Information_search.get_all_records()

def search_title(title):
    return Information_search.search_title(title)
    
def search_director(director):
    return Information_search.search_director(director)

def search_year(year):
    return Information_search.search_year(year)

def search_genre(genre):
    return Information_search.search_genre(genre)
      
        
if __name__ == "__main__":
    pass