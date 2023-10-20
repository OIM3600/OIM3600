import csv
import urllib.request
import json
import pprint


def get_country_info(name):
    """
    Get weather data for a specified city and country using the OpenWeatherMap API.
    """
    name = name.replace(' ', '%20')
    api_url = f'https://restcountries.com/v3.1/name/{name}'
    print(api_url)

    with urllib.request.urlopen(api_url) as response:
        response_text = response.read().decode('utf-8')
        country_info = json.loads(response_text)

    return country_info[0]


def display_country_info(data):
    """"""
    pprint.pprint(data)


def write_csv():
    """"""
    countries = [
        'usa',
        'brazil',
        'thailand',
        'puerto rico',
        'japan',
        'switzerland',
        'mexico',
        'iceland',
        'south korea',
        'peru',
        'turkey',
        'sweden',
        'denmark',
        'britain',
        'australia',
    ]
    with open('data/countries.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(('code', 'name', 'continent', 'population', 'capital'))
        for country in countries:
            print(country)
            data = get_country_info(country)
            code = data['cca2']
            name = data['name']['common']
            continent = data['continents'][0]
            population = data['population']
            capital = data['capital'][0]
            csv_writer.writerow((code, name, continent, population, capital))


def main():
    """"""
    # info = get_country_info('usa')
    # pprint.pprint(info)
    # display_country_info(info)
    write_csv()


main()
