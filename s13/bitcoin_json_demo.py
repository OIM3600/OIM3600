import pprint

data = {
    "time": {
        "updated": "Oct 9, 2024 15:02:58 UTC",
        "updatedISO": "2024-10-09T15:02:58+00:00",
        "updateduk": "Oct 9, 2024 at 16:02 BST",
    },
    "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
    "chartName": "Bitcoin",
    "bpi": {
        "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "61,824.03",
            "description": "United States Dollar",
            "rate_float": 61824.0304,
        },
        "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "47,285.553",
            "description": "British Pound Sterling",
            "rate_float": 47285.5532,
        },
        "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "56,442.31",
            "description": "Euro",
            "rate_float": 56442.3104,
        },
    },
}


# Find the current bitcoin price in USD
# pprint.pprint(data)

# print(type(data))
# print(data.keys())
# pprint.pprint(data["bpi"])

bpi = data["bpi"]
# print(type(bpi))
# print(bpi.keys())

pprint.pprint(bpi["USD"])

print(data["bpi"]["USD"]["rate"])
