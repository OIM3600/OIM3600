import csv


# def read_countries():
#     """Read the data from countries.csv"""
#     with open("data/countries.csv", "r") as file:
#         # reader = csv.reader(file)
#         # next(reader)
#         # for row in reader:
#         #     name = row[1]
#         #     continent = row[2]
#         #     print(name, continent)
#         reader = csv.DictReader(file)
#         for row in reader:
#             name = row["name"]
#             continent = row["continent"]
#             print(name, continent)


def read_countries():
    """Read the data from countries.csv, and get the numbers by continent"""
    with open("data/countries.csv", "r") as file:
        reader = csv.DictReader(file)
        continent_counts = {}  # {'Asia': 2, 'North America': 1, ...}
        for row in reader:
            name = row["name"]
            continent = row["continent"]
            continent_counts[continent] = continent_counts.get(continent, 0) + 1

        # print(continent_counts)
        user_input = input("Enter a continent: ")
        print(continent_counts[user_input])


read_countries()
