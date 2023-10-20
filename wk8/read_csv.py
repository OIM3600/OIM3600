import csv

with open('data/countries.csv', 'r') as file:
    reader = csv.DictReader(file)
    # asia, europe, north_america = 0, 0, 0
    counts = {}
    for row in reader:
        name = row['name']
        continent = row['continent']
        print(f'{name}, {continent}')
        if continent not in counts:
            counts[continent] = 1
        else:
            counts[continent] += 1
        # if continent == 'Asia':
        #     asia += 1
        # elif continent == 'Europe':
        #     europe += 1
        # elif continent == 'North America':
        #     north_america += 1

    # print(counts)
    continent = input('Enter a continent: ')
    if continent in counts:
        print(f'{continent}: {counts[continent]}')
