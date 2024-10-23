import urllib.request
import json
import pprint
import csv


def get_data_from_url(url):
    """
    Get data from a URL and handle potential errors.
    """
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            data = json.loads(response_text)
        return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(f"Data not found for the given URL: {url}")
        else:
            raise RuntimeError(f"HTTP Error occurred: {e.code}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Failed to reach the server: {e.reason}")
    except json.JSONDecodeError:
        raise ValueError("Failed to parse JSON response.")


def get_country_data(url):
    """
    A generic function to get country data by URL.
    """
    try:
        return get_data_from_url(url)[0]
    except (IndexError, ValueError) as e:
        print(f"Error retrieving country data: {e}")
        return None


def get_country_info(country_name):
    """
    Get country data for a specified country using REST Countries API.
    """
    country_name = country_name.replace(" ", "%20")
    api_url = f"https://restcountries.com/v3.1/name/{country_name}"
    return get_country_data(api_url)


def get_country_info_by_code(code):
    """
    Get country data using REST Countries API by country code.
    """
    api_url = f"https://restcountries.com/v3.1/alpha/{code}"
    return get_country_data(api_url)


def display_country_info(country_info):
    """
    Pretty print the country information. Can be used for debugging.
    """
    if country_info:
        pprint.pprint(country_info)
    else:
        print("No country information available.")


def get_neighboring_countries(country_name):
    """
    Get the neighboring countries of the specified country by their full names.
    """
    country_info = get_country_info(country_name)
    if country_info is None:
        print(f"Could not retrieve country data for {country_name}.")
        return []

    neighbors = country_info.get("borders", [])  # Handle cases with no borders
    full_names = []

    for abbr in neighbors:
        country = get_country_info_by_code(abbr)
        if country:
            full_names.append(country["name"]["official"])
        else:
            print(f"Could not retrieve data for country code {abbr}.")

    return full_names


# Ask for country names and store country info in csv.
# use while loop to ask names
# create a csv
# country_name, population, continent, ....
# Canada,


def get_country_list_from_input():
    """
    Ask the user to input country names. Ends when the user types 'done'.
    """
    countries = []
    print("Enter country names (type 'done' when finished):")

    while True:
        country = input("Country name: ").strip()
        if country.lower() == "done":
            break
        if country:
            countries.append(country)

    return countries


def export_country_data_to_csv(countries):
    """
    Write country data into a CSV file based on user input.
    """
    if not countries:
        print("No countries entered. Exiting.")
        return

    print(f"Fetching data for countries: {countries}")

    with open("data/countries.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(("code", "name", "continent", "population", "capital"))

        for country in countries:
            info = get_country_info(country)
            if info is None:
                print(f"Skipping country {country}, data not found.")
                continue

            code = info.get("cca2", "N/A")
            name = info["name"].get("common", "N/A")
            continent = info.get("continents", ["N/A"])[0]
            population = info.get("population", "N/A")
            capital = info.get("capital", ["N/A"])[0]

            csv_writer.writerow((code, name, continent, population, capital))
            print(f"Added {name} to CSV.")


def main():
    """
    Main function to drive the program.
    """
    countries = get_country_list_from_input()

    export_country_data_to_csv(countries)


if __name__ == "__main__":
    main()
