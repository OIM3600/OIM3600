import webbrowser


def count_freq(s):
    """
    Calculates each item's frequency in a given string/list
    To represent the returned value, we could choose dict
    """
    freqs = {}  # initialize the variable to return
    for item in s:
        if item not in freqs:
            freqs[item] = 1
        else:
            freqs[item] += 1
    return freqs


def read_data():
    """Read data from data/mess.txt, return a long string"""
    with open("data/mess.txt", "r", encoding="utf8") as file:
        data = file.read()
        return data


def make_word_from_freq(d):
    """Find all the characters whose freq is 1 in d and make the word"""
    res = ''
    for k, v in d.items():
        if v == 1:
            res += k
    return res


def main():
    # Read data from data/mess.txt
    data = read_data()
    # Get character freqs
    freqs = count_freq(data)
    # Find the rare ones
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    new_url = url.replace("ocr", make_word_from_freq(freqs))
    webbrowser.open(new_url)



main()