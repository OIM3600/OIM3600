def search(numbers, target):
    """Binary search
    Return the index of target in numbers. Return False if the target is not in numbers.
    """
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        if target == numbers[mid]:
            return mid  # Found!
        elif target < numbers[mid]:  # target might be in the left half
            right = mid - 1
        else:  # target might be in the right half
            left = mid + 1

    return False


def main():
    numbers = [1, 5, 10, 20, 50, 100, 500]
    to_find = int(input("Number: "))
    print(search(numbers, to_find))


main()
