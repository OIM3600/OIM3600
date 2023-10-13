import time
import random


def bubble_sort(arr):
    '''Bubble sort'''
    n = len(arr)

    for i in range(n):
        # last i elements are already sorted, so we don't have to compare them again
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_improved(arr):
    '''Bubble sort'''
    n = len(arr)

    for i in range(n):
        swapped = False  # flag if any swap occured in this run
        # last i elements are already sorted, so we don't have to compare them again
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def main():
    # numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    # numbers = [random.randint(0, 10000) for _ in range(10000)]
    numbers = list(range(10000))
    start = time.time()
    bubble_sort(numbers)
    # bubble_sort_improved(numbers)
    end = time.time()
    print(f'Running time:  {end-start}s')
    # print(numbers)


main()
