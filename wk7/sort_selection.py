def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


def main():
    numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    selection_sort(numbers)
    print(numbers)


if __name__ == "__main__":
    main()
