import csv


# with open('data/countries.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader) # skip first row
#     for row in reader:
#         print(row[2]) # We need to remember which column


# with open("data/countries.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         name = row["name"]
#         continent = row["continent"]
#         print(f"{name}, {continent}")


# Find out how many countries in each continent
# asia: 5, europ: 3
with open("data/countries.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}  # str: int

    for row in reader:
        name = row["name"]
        continent = row["continent"]
        # if continent not in counts:
        #     counts[continent] = 1
        # else:
        #     counts[continent] += 1
        counts[continent] = counts.get(continent, 0) + 1

    print(counts)

    user_input = input("Continent: ")
    if user_input in counts:
        print(counts[user_input])
    else:
        print("Not found in data.")
