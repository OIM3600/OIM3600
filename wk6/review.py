"""
Write a function to check if a given string does not contain any vowel letters (i.e., 'a', 'e', 'i', 'o', 'u').
"""


def no_vowel(s):
    """
    Return True if s does not contain any vowel letter, return False otherwise
    """
    # check every letter in s
    #     if letter is vowel
    #         return False
    #     else continue

    # return True

    for letter in s:
        if letter in "aeiouAEIOU":
            break  # immediately jump/exit out of the for loop
            return False  # immediately ends the function
        # else:
        #     continue

    return True


# print(no_vowel("abc"))  # False
# print(no_vowel("bbc"))  # True
# print(no_vowel("babson"))  # False
# print(no_vowel("Alex"))  # False


# To solve spelling bee puzzle
# get a list of all the english words
# check each word:
#     1. >= 4 letters
#     2. it must contain the center letter
#     3. it cannot use invalid letters


# nums = [1, 1, 2, 3, 5, 8, 13]

# # mean
# print(sum(nums) / len(nums))

# # median

# median = nums[len(nums) // 2]
# print(median)


def median(nums):
    """
    return median of the given list of sorted numbers
    """
    n = len(nums)
    if n % 2 == 1:  # odd number of numbers
        return nums[n // 2]
    else:
        # return (nums[n // 2 - 1] + nums[n // 2]) / 2
        return sum(nums[n // 2 - 1 : n // 2 + 1]) / 2


nums1 = [1, 1, 2, 3, 5, 8, 13]
nums2 = [1, 1, 2, 3, 5, 8, 13, 21]  # len: 8, get index 3, 4

print(median(nums1))  # 3
print(median(nums2))  # 4 = (3 + 5) / 2


# keep asking user to enter numbers, until entering 'stop', calculate some statistics results.
