# How do check if a given string does not contain any vowel letters (i.e., 'a', 'e', 'i', 'o', 'u')?


def has_no_vowel(s):
    """Return True if s has no vowel letters (aeiou)"""
    s = s.lower()

    for letter in s:
        # print(letter)
        if letter in 'aeiou':
            return False

    return True


# print(has_no_vowel('BCD'))  # True
# print(has_no_vowel('Python'))  # False


# How can you find the mean of nums without using external libraries? the median?


def find_mean(data):
    """return the mean of a given list of numbers, data

    find total: using a for loop
    find # of items: len(data)
    total/#of itmes
    """
    # return sum(data) / len(data)
    total = 0
    for x in data:
        total += x

    return total / len(data)


def find_median(data):
    """return the median of a given list of numbers, data"""
    data.sort()
    n = len(data)
    if n % 2 == 1:  # the length of the list is an odd number
        return data[n // 2]
    else:  # even number
        # [1, 1, 2, 3, 5, 8, 13, 21]  8 numbers
        #           ^  ^
        #           8//2 -1, 8//2
        return (data[n // 2 - 1] + data[n // 2]) / 2


# nums = [1, 1, 2, 3, 5, 8, 13]
# print(find_mean(nums))
# print(find_median(nums))

# nums.append(21)
# print(find_mean(nums))
# print(find_median(nums))


# How can you create a dictionary letter_count that counts the frequency of each letter in a given string?


def letter_count(s):
    """return the frequencies of letters in s
    in a dict format
    """
    counter = {}

    for letter in s:
        # if letter not in counter:
        #     counter[letter] = 1
        # else:
        #     counter[letter] += 1
        counter[letter] = counter.get(letter, 0) + 1
    return counter


print(letter_count('Okeeffe'))  # {e: 3, f:2, 'O': 1, 'k':1}
