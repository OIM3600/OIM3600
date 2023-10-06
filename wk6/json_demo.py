data = {
    "time": {
        "updated": "Oct 6, 2023 16:19:00 UTC",
        "updatedISO": "2023-10-06T16:19:00+00:00",
        "updateduk": "Oct 6, 2023 at 17:19 BST",
    },
    "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
    "chartName": "Bitcoin",
    "bpi": {
        "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "27,790.9365",
            "description": "United States Dollar",
            "rate_float": 27790.9365,
        },
        "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "23,221.8842",
            "description": "British Pound Sterling",
            "rate_float": 23221.8842,
        },
        "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "27,072.4297",
            "description": "Euro",
            "rate_float": 27072.4297,
        },
    },
}

import pprint

pprint.pprint(data)

price_usd = data['bpi']['USD']['rate_float']
print(price_usd)

price_euro = data['bpi']['EUR']['rate_float']
print(price_euro)
