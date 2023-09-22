def get_height():
    """
    Ask user for the size of grid and return the value
    """
    while True:
        n = int(input('Height: '))
        if 1 <= n <= 8:
            return n


def print_triangle(n):
    """
    Print the triangle with given height
    """
    for i in range(n):
        for j in range(i + 1):
            print('#', end='')
        print()


def print_triangle_2(n):
    """
    Print the other triangle with given height
    """
    for i in range(n):
        # for j in range(n - i - 1):
        #     print(' ', end='')
        # for j in range(i + 1):
        #     print('#', end='')
        # print()
        print(' ' * (n - i - 1) + '#' * (i + 1))


# Get height of triangle
n = get_height()

# print triangle of bricks
# print_triangle(n)
print_triangle_2(n)
