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
    """
    Merge Sort
    Return a (new) sorted list of numbers
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def main():
    numbers = [7, 2, 5, 4, 1, 6, 0, 3]
    sorted_numbers = merge_sort(numbers)
    print(sorted_numbers)


if __name__ == "__main__":
    main()
