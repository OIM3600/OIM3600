data = {
    "time": {
        "updated": "Feb 23, 2024 16:39:10 UTC",
        "updatedISO": "2024-02-23T16:39:10+00:00",
        "updateduk": "Feb 23, 2024 at 16:39 GMT",
    },
    "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
    "chartName": "Bitcoin",
    "bpi": {
        "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "50,973.809",
            "description": "United States Dollar",
            "rate_float": 50973.8093,
        },
        "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "40,209.415",
            "description": "British Pound Sterling",
            "rate_float": 40209.4151,
        },
        "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "47,107.14",
            "description": "Euro",
            "rate_float": 47107.14,
        },
    },
}


from pprint import pprint

# pprint(data)


# get the current price in USD

price = data["bpi"]["USD"]["rate_float"]

pprint(price)

# get the current price in EUR

price_eur = data["bpi"]["EUR"]["rate_float"]
