def linear_search(numbers, target):
    """Return the index of target if target is found in the given list of numbers, -1 if not"""
    # for num in numbers:
    #     if num == target:
    #         return True
    # return False

    for i in range(len(numbers)):
        if numbers[i] == target:
            print('Found!')
            return i
    print('Not found.')
    return -1


def main():
    # numbers = [20, 500, 10, 5, 100, 1, 50]
    # to_find = int(input('Number to find: '))
    # print(linear_search(numbers, to_find))  #
    names = ['Naomi', 'Emory', 'Arvaan', 'Siying', 'Kevin', 'Ryan']
    to_find = input('Number to find: ')
    print(linear_search(names, to_find))


main()
