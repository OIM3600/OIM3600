def search(nums, target):
    """
    Linear search
    return the index of the target in nums if it is in the list
    return -1 otherwise
    """
    for i in range(len(nums)):
        if nums[i] == target:
            print("Found!")
            return i
    return -1


def main():
    numbers = ["Young", "Leule", "Brandon", "Hanlu", "Alex"]
    to_find = input("Number to find: ")
    idx = search(numbers, to_find)
    print(idx)


main()
