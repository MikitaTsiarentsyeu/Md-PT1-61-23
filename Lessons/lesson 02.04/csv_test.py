import csv

# separator = ','

headline = ['make', 'model', 'volume', 'power', 'year']
new_headline = ['make', 'model', 'year']

with open('cars.csv', 'r') as f:
    reader = csv.DictReader(f, headline)
    res = [{head:line[head] for head in new_headline} for line in reader]


with open('new_cars.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, new_headline)
    writer.writerows(res)

# with open('cars.csv', 'r') as f:
#     reader = csv.reader(f)
#     res = [[i[0], i[1], i[-1]] for i in reader]
#     # for values in reader:
#     #     print(values)

# print(res)

# with open('new_cars.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(res)

# with open('cars.csv', 'r') as f:
#    "ideal world"
#     with open('new_cars.csv', 'w') as new:
#         for line in f:
#             values = line.split(separator)
#             new.write(separator.join([values[0], values[1], values[-1]]))

# transit = []

# with open('cars.csv', 'r') as f:
#     for line in f:
#         values = line.split(separator)
#         transit.append(separator.join([values[0], values[1], values[-1]]))

# with open('new_cars.csv', 'w') as new:
#     new.writelines(transit)