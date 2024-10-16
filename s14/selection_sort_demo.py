def sort(numbers):
    """
    Selection Sort
    Return a sorted list of numbers
    """
    n = len(numbers)
    for i in range(n):
        # Find the smallest in the remaining unsorted list
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Swap the smallest number with numbers[i]
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


def main():
    numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    sort(numbers)
    print(numbers)


main()
