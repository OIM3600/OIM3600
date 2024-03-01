def search(nums, target, left, right):
    """
    Binary search using recursion
    return the index of the target in nums if it is in the list
    return -1 otherwise
    """
    if left <= right:
        mid = left + (right - left) // 2  # calcuate middle index
        if nums[mid] == target:
            print("Found!")
            return mid
        elif nums[mid] < target:
            return search(nums, target, mid + 1, right)  # Target is in the right half
        else:
            return search(nums, target, left, mid - 1)  # Target is in the left half
    else:
        return -1


def main():
    numbers = [1, 5, 10, 20, 50, 100, 500]
    #                        |   |     |
    #                        l   mid   r

    to_find = int(input("Number to find: "))
    idx = search(numbers, to_find, 0, len(numbers) - 1)
    print(idx)


main()
