import csv
import urllib.request
import json
import pprint


def get_country_info(name):
    """
    Get country data for acountry using the retstcountries API.
    """
    name = name.replace(" ", "%20")
    api_url = f"https://restcountries.com/v3.1/name/{name}"
    # print(api_url)

    with urllib.request.urlopen(api_url) as response:
        response_text = response.read().decode("utf-8")
        country_data = json.loads(response_text)

    return country_data[0]


def write_csv():
    """
    Write data about several countries in to a csv file.
    """
    countries = [
        "Switzerland",
        "Thailand",
        "North Korea",
        "Japan",
        "South Korea",
        "Iceland",
        "Mongolia",
        "Republic of India",
        "Germany",
        "South Africa",
        "Argentina",
        "Peru",
    ]

    with open("data/countries.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(("code", "name", "continent", "population", "capital"))

        for country in countries:
            info = get_country_info(country)
            code = info["cca2"]
            name = info["name"]["common"]
            continent = info["continents"][0]
            population = info["population"]
            capital = info["capital"][0]
            csv_writer.writerow((code, name, continent, population, capital))


def main():
    # info = get_country_info("usa")
    # pprint.pprint(info)
    write_csv()


main()
