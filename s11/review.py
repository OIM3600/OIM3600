# Write a function to check if a given string contains no vowels (i.e., none of letters 'a', 'e', 'i', 'o', 'u').


def contains_no_vowel(s):
    """
    Returns True if there is no vowel letters, otherwise return False

    Check every letter in the string:
        if the letter is vowel:
            return False # return will end the function
        else:
            return True
    """
    for letter in s:
        if letter in "aeiouAEIOU":
            return False  # return will end the function
        # else:
        #     # return True  # return will end the function
        #     continue

    return True  # only return True after checking all letters, which means no False is returned


print(contains_no_vowel("abc"))  # False
print(contains_no_vowel("bbc"))  # True
print(contains_no_vowel("babson"))  # False
print(contains_no_vowel("BABSON"))  # False


# Think about solving spelling bee puzzle from nytimes.com

# Yesterday (20241001) is a perfect square number. Can you find the next one?


# How can you find the mean of a list of numbers without using external libraries? What about the median?


def mean(nums):
    """
    Returns the mean of a list of numbers
    """
    return sum(nums) / len(nums)


def median(nums):
    """Returns the median of a list of numbers"""
    # sort the list first, but do not sort in-place
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        return  # get the middle number
    else:
        return  # calculate the average of the middle two numbers


numbers = [10, 48, 10, 2, 2024]
print(mean(numbers))  # ?
print(median(numbers))  # 10


# How to achieve this? Your program should keep asking user to enter a number, until entering 'stop', then calculate the mean and median.


