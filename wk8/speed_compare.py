import bisect
import time


def create_list():
    """Return a list of words"""
    data = []
    with open("data/words.txt", "r") as file:
        for line in file:
            word = line.strip()
            data.append(word)
    return data


def create_set():
    """Return a set of words"""
    data = set()
    with open("data/words.txt", "r") as file:
        for line in file:
            word = line.strip()
            data.add(word)
    return data


def main():
    word_list = create_list()
    print(len(word_list))

    word_set = create_set()
    print(len(word_set))

    word = input('Enter a word to search: ')

    # Measure time for searching in a list
    start_time = time.time()
    for _ in range(1000):
        if word in word_list: # linear search
            pass
        else:
            pass
    end_time = time.time()
    print(f'Time taken to search in list: {end_time-start_time:.8f}s')
    
    # Measure time for searching in a set
    start_time = time.time()
    for _ in range(1000):
        if word in word_set:
            pass
        else:
            pass
    end_time = time.time()
    print(f'Time taken to search in set: {end_time-start_time:.8f}s')

    # Measure time for searching in a list
    start_time = time.time()
    for _ in range(1000):
        idx = bisect.bisect_left(word_list, word)
    end_time = time.time()
    print(f'Time taken to binary search in list: {end_time-start_time:.8f}s')
    

main()
