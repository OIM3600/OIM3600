import random
import time


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list
    """
    result, left_idx, right_idx = [], 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


def merge_sort(arr):
    """Merge sort"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def main():
    # numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    # sorted_numbers = merge_sort(numbers)
    # print(sorted_numbers)

    numbers = [random.randint(0, 10000) for _ in range(10000)]
    # numbers = list(range(10000))
    start = time.time()
    merge_sort(numbers)
    # bubble_sort_improved(numbers)
    end = time.time()
    print(f'Running time:  {end-start}s')


if __name__ == "__main__":
    main()
