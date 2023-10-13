def selection_sort(arr):
    """Selection sort"""
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # find the current min
                min_index = j

        # swap the found min with the first element of the remaining unsorted array, i
        arr[i], arr[min_index] = arr[min_index], arr[i]


def main():
    numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    selection_sort(numbers)
    print(numbers)


main()
