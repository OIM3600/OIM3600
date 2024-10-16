def bubble_sort(arr):
    """
    Bubble Sort
    Return a sorted list of numbers
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to compare them again
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_improved(arr):
    """
    Bubble Sort
    Return a sorted list of numbers
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Used to flag if any swap occurred in this pass

        # Last i elements are already in place, so we don't need to compare them again
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            # If no swaps occurred in a pass, the list is already sorted, so we can stop
            break


def main():
    numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    bubble_sort(numbers)
    print(numbers)


if __name__ == "__main__":
    main()
