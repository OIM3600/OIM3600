import time
import bisect


def load_words_into_list():
    """Read all the English words from words.txt into a list and return the list"""
    words = []
    with open("data/words.txt") as file:
        for line in file:
            word = line.strip()  # remove the trailing \n in end of each line
            words.append(word)
    return words


def load_words_into_dict():
    """Read all the English words from words.txt into a dict and return the dict"""
    words = {}
    with open("data/words.txt") as file:
        for line in file:
            word = line.strip()  # remove the trailing \n in end of each line
            words[word] = 1
    return words


def load_words_into_set():
    """Read all the English words from words.txt into a set and return the set"""
    words = set()
    with open("data/words.txt") as file:
        for line in file:
            word = line.strip()  # remove the trailing \n in end of each line
            words.add(word)
    return words


def search_word(word, words):
    """Return whether word is in words. words can be a list, dict, set"""
    return word in words


def binary_search(word, words):
    """Using bisect to search a word in a list"""
    index = bisect.bisect_left(words, word)
    return index < len(words) and words[index] == word


def main():
    words_list = load_words_into_list()
    words_dict = load_words_into_dict()
    words_set = load_words_into_set()
    # print(words_list[-1], len(words_list))
    # print(len(words_dict))
    # print(len(words_set))

    word = "python"

    # Measure the time for searching in a list
    start_time = time.time()
    for _ in range(10_000):
        search_word(word, words_list)
    duration = time.time() - start_time
    print(f"Time to search in a list: {duration:.8f} seconds")

    # Measure the time for searching in a dict
    start_time = time.time()
    for _ in range(10_000):
        search_word(word, words_dict)
    duration = time.time() - start_time
    print(f"Time to search in a dict: {duration:.8f} seconds")

    # Measure the time for searching in a set
    start_time = time.time()
    for _ in range(10_000):
        search_word(word, words_set)
    duration = time.time() - start_time
    print(f"Time to search in a set: {duration:.8f} seconds")

    # Measure the time for searching in a list using binary search
    start_time = time.time()
    for _ in range(10_000):
        binary_search(word, words_list)
    duration = time.time() - start_time
    print(f"Time to binary search in a list: {duration:.8f} seconds")


main()
