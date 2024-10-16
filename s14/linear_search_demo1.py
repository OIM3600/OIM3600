def search(numbers, target):
    """Linear Search
    Return the index of target in numbers. Return False if the target is not in numbers.
    """
    n = len(numbers)
    for i in range(n):
        if target == numbers[i]:
            print("Found!")
            return i
    print("Not found!")
    return False


def main():
    numbers = [20, 500, 10, 5, 100, 1, 50]
    to_find = int(input("Number: "))
    print(search(numbers, to_find))


main()
