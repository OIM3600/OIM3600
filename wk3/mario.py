def get_size() -> int:
    """Get the size, then return the number"""
    while True:
        n = int(input('Size: '))
        if n > 0:
            return n


def print_grid(n):
    """print the grid of bricks"""
    for i in range(n):
        for j in range(n):
            print('#', end='')
        print()


def main():
    size = get_size()  # the function get_size is called
    print_grid(size)


main()
