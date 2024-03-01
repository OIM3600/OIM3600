def search(nums, target):
    """
    Binary search
    return the index of the target in nums if it is in the list
    return -1 otherwise
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # calcuate middle index
        if nums[mid] == target:
            print("Found!")
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1


def main():
    numbers = [1, 5, 10, 20, 50, 100, 500]
    #                        |   |     |
    #                        l   mid   r

    to_find = int(input("Number to find: "))
    idx = search(numbers, to_find)
    print(idx)


main()
