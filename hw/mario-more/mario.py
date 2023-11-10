def get_height():
    """
    Ask user for the size of grid and return the value
    """
    while True:
        n = int(input('Height: '))
        if 1 <= n <= 8:
            return n


def print_pyramid(n):
    """ """
    for i in range(n):
        print(
            '.' * (n - i - 1)
            + '#' * (i + 1)
            + '.' * 2
            + '#' * (i + 1)
            + '.' * (n - i - 1)
        )


# Get height of pyramid
n = get_height()

print_pyramid(n)
