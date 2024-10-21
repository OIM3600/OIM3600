def sort(arr):
    """
    Selection Sort
    Return a sorted list of numbers
    """
    n = len(arr)
    for i in range(n):
        # Find the smallest in the remaining unsorted list
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the smallest number with numbers[i]
        arr[i], arr[min_index] = arr[min_index], arr[i]


def main():
    numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    sort(numbers)
    print(numbers)


main()
