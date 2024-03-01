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
    numbers = [20, 500, 10, 5, 100, 1, 50]
    to_find = int(input("Number to find: "))
    idx = search(numbers, to_find)
    print(idx)


main()
