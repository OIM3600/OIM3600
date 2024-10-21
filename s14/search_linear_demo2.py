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
    numbers = ["Tobi", "Jane", "Anton", "Amelia", "Sam", "Deepali"]
    to_find = input("Number: ")
    print(search(numbers, to_find))


main()
