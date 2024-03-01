import string
import random

# URL -> shorter URL
long_to_short = {
    "www.babson.edu": "etw456",
}

# shorter URL -> original URL
short_to_long = {
    "etw456": "www.babson.eud",
}


def shorten(original_url):
    """
    Return the shortened url, also save it into two dicts
    """
    # www.babson.edu
    # if the URL is in long_to_short, return the short
    # else: shorten it, store it in both dicts, return the short
    if original_url in long_to_short:
        print("URL exists!")
        return long_to_short[original_url]

    availables = string.ascii_letters + string.digits

    # short = ''
    # for i in range(6):
    #     short += random.choice(availables)
    short = "".join(random.choices(availables, k=6))
    long_to_short[original_url] = short
    short_to_long[short] = original_url

    return short


result = shorten("www.babson.edu")
result = shorten("www.google.com")
print(result)

print(long_to_short)
print(short_to_long)
