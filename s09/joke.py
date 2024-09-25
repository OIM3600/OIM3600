import json
import urllib.request

URL = "https://v2.jokeapi.dev/joke/Any?safe-mode"

try:
    with urllib.request.urlopen(URL) as response:
        data = response.read()
        json_data = json.loads(data)
        if json_data["type"] == "single":
            print(json_data["joke"])
        elif json_data["type"] == "twopart":
            print(json_data["setup"])
            print(json_data["delivery"])
except urllib.error.URLError as e:
    print(f"Error fetching data from URL: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON data: {e}")
