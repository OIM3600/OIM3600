import json
import urllib.request


def get_bitcoin_price():
    """Get the current price of Bitcoin in USD from the CoinDesk API."""
    # return 10000.00
    URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    with urllib.request.urlopen(URL) as response:
        data = response.read()
        data = json.loads(data)
        price_in_usd = float(data["bpi"]["USD"]["rate_float"])
        return price_in_usd


def main():
    print(get_bitcoin_price())


if __name__ == "__main__":
    main()
