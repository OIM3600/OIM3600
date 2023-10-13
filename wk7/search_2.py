def binary_search(arr, target):
    """Binary search"""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # calculate the middle index
        if arr[mid] == target:
            print('Found!')
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print('Not found.')
    return -1


def main():
    numbers = [1, 5, 10, 20, 50, 100, 500] # a sorted list
    to_find = int(input("Number to find: "))
    print(binary_search(numbers, to_find))


main()
