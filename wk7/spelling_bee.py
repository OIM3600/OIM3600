def spelling_bee():
    """
    print all the qualified words

    pseudo-code:
    Iterate through the words.txt,
    if the word has at least 4 letters and contains the center letter and only uses the required letters , print it

    """
    with open("data/words.txt", "r") as file:
        for line in file:
            word = line.strip()
            if len(word) >= 4 and "f" in word and only_use(word, "lnbaief"):
                print(word)


def only_use(word, letters):
    """
    Return True if word only uses given letters, return False otherwise
    """
    for c in word:
        if c not in letters:
            return False

    return True


# print(only_use("fable", "lnbaief"))  # True
# print(only_use("babson", "lnbaief"))  # False

spelling_bee()
