import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather_data(city_name, country_code, api_key):
    """
    Get weather data for a specified city and country using the OpenWeatherMap API.
    """
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&APPID={api_key}&units=imperial"

    with urllib.request.urlopen(api_url) as response:
        response_text = response.read().decode("utf-8")
        weather_data = json.loads(response_text)

    return weather_data


def get_temp(city):
    """
    Get the temperature from the weather data.
    """
    # return 100  # fake it for now, until you make it
    country = "us"
    weather_data = get_weather_data(city, country, APIKEY)
    return weather_data["main"]["temp"]


def main():
    city_name = "Wellesley"
    # country_code = "us"

    # weather_data = get_weather_data(city_name, country_code, APIKEY)
    # print(weather_data)
    print(get_temp(city_name))


if __name__ == "__main__":
    main()
