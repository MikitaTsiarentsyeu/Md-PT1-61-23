import json
import csv


headline = ['make', 'models', 'year', 'trim_level', 'price']

with open("cars.json", "r") as file:
    data = json.load(file)
    with open('new_cars.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, headline)
        writer.writeheader()

        cars_dict = {}
        for i in data[0]['models']:
            
            cars_dict['make'] = 'Toyota'
            cars_dict['models'] = i['name']
            cars_dict['year'] = i['year']
            for j in i['trim_levels']:
                cars_dict['trim_level'] = j['name']
                cars_dict['price'] = j['price']
                writer.writerow(cars_dict)
            
        for i in data[1]['models']:
            
            cars_dict['make'] = 'Honda'
            cars_dict['models'] = i['name']
            cars_dict['year'] = i['year']
            for j in i['trim_levels']:
                cars_dict['trim_level'] = j['name']
                cars_dict['price'] = j['price']
                writer.writerow(cars_dict)

