# import os

# print(os.getcwd())

# with open("data/data.txt", "r") as f:
#     # data = f.read()
#     # print(data)
#     for line in f:
#         print(line.rstrip("\n"))


# with open("data/data.txt", "a") as f:
#     f.write("Hello, world\n")

import csv

# data = [
#     ["Stock", "Share"],
#     ["MSFT", 25],
#     ["GOOG", 30],
# ]

# with open("data/data.csv", "w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)

#     # csv_writer.writerows(data)
#     for row in data:
#         csv_writer.writerow(row)


with open("data/data.csv", "r") as csv_file:
    for line in csv_file:
        print(line.strip("\n"))
