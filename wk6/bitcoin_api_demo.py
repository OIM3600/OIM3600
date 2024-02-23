import json
import urllib.request
from pprint import pprint

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
u = urllib.request.urlopen(URL)

with urllib.request.urlopen(URL) as response:
    data = response.read()
    json_data = json.loads(data)  # in dict type

    # pprint(json_data)
    price_in_usd = json_data["bpi"]["USD"]["rate_float"]

    print(price_in_usd)

    price_in_eur = json_data["bpi"]["EUR"]["rate_float"]
    print(price_in_eur)
