def read_data(filename):
    """return the data (a list of words) from the file"""
    with open(filename, 'r') as f:
        data = f.readlines()
        # print(type(data))

    word_list = []
    for line in data:
        word_list.append(line.strip())

    return word_list


# print(read_data('data/words.txt'))


def use_only(word, letters):
    """
    Check if the word only uses the letters, return True if so, return False otherwise
    """
    # word: bolt, letters: 'bloihnt'
    for letter in word:
        if letter not in letters:
            return False
        # else:
        #     return True # immediately ends the function
    return True


# print(use_only('bolt', 'bloihnt')) # True
# print(use_only('bolter', 'bloihnt')) # False


def spell_bee(word_list, center, letters):
    """
    Find all the qualified words from a given word list, print them
    Rules are:
    1. >= 4 letter
    2. contains center letter
    3. uses only the given letters
    """
    # look at every word in word list, if the word is qualified, print it
    for word in word_list:
        # if the word has 4 or more letters and the word uses center and the word only uses the letters
        if len(word) >= 4 and center in word and use_only(word, letters):
            print(word)


# spell_bee()


def main():
    center = 't'
    letters = 'bloihnt'
    word_list = read_data('data/words.txt')
    spell_bee(word_list, center, letters)

main()