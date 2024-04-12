import urllib.request
import json
from config import OPENWEATHER_APIKEY


def get_weather_data(city_name):
    """
    Get weather data for a specified city and country using the OpenWeatherMap API.
    """
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={OPENWEATHER_APIKEY}&units=imperial"
    # print(api_url)

    with urllib.request.urlopen(api_url) as response:
        response_text = response.read().decode("utf-8")
        weather_data = json.loads(response_text)

    return weather_data["main"]["temp"]
