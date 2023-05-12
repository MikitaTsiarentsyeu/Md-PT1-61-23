import csv

def list_collection(): 
    with open('Tasks/Nikiforov/Task7/list_of_movies.csv', 'r') as f:
        list_of_movies = [row.split(',') for row in f]
        return list_of_movies

def file_write(new_movie): 
    with open('Tasks/Nikiforov/Task7/list_of_movies.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_movie)

def search_title():
    title = input("Enter the title of the movie:\n").title().strip()
    with open('Tasks/Nikiforov/Task7/list_of_movies.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == title:
                    yield ' '.join(row)
                 
def search_director(): 
    director = input("Enter the director of the movie:\n").title().strip()
    with open('Tasks/Nikiforov/Task7/list_of_movies.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == director:
                    yield ' '.join(row)
                
def search_year(): 
    year = input("Enter the year the movie was released:\n").strip()
    with open('Tasks/Nikiforov/Task7/list_of_movies.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == year:
                    yield ' '.join(row)

def search_genre():
    genre = input("Enter the genre of the movie:\n")
    with open('Tasks/Nikiforov/Task7/list_of_movies.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[3] == genre:
                    yield ' '.join(row)

                
if __name__ == '__main__':
    for i in search_title():
        print(i)
    for i in search_director():
        print(i)
    for i in search_year():
        print(i)
    for i in search_genre():
        print(i)


                