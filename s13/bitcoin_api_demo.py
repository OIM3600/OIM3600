import urllib.request
import json

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

with urllib.request.urlopen(URL) as response:
    data = response.read()
    data = json.loads(data)
    # print(data)
    # print(type(data))
    price_in_usd = float(data["bpi"]["USD"]["rate_float"])
    print(price_in_usd)