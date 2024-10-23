def search(numbers, target, left, right):
    """Binary search recursively
    Return the index of target in numbers. Return False if the target is not in numbers.
    """
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        if target == numbers[mid]:
            return mid  # Found!
        elif target < numbers[mid]:  # target might be in the left half
            return search(numbers, target, left, mid - 1)
        else:  # target might be in the right half
            return search(numbers, target, mid + 1, right)

    return False


def main():
    numbers = [1, 5, 10, 20, 50, 100, 500]
    to_find = int(input("Number: "))
    print(search(numbers, to_find, 0, len(numbers) - 1))


main()
