def get_dict():
    with open('data/nutrition_list.txt') as file:
        data = file.readlines()
    d = {}
    for line in data:
        fruit, calories = line.strip().split(', ')
        d[fruit] =  int(calories)
    return d

def get_calories(data, fruit):
    """"""