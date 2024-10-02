import os


print(os.getcwd())

# with open("data/foo.txt", "r", encoding="utf8") as file:
#     data = file.read()
#     print(data)
#     print(data.split())


# with open('data/outfile.txt', 'w') as file:
#     file.write('Hey jude, dont make it bad')


import csv

data = [
    ["Stock", "Share"],
    ["MSFT", 25],
    ["GOOG", 30],
]

with open("data/data.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # csv_writer.writerows(data) # or
    for row in data:
        csv_writer.writerow(row)
