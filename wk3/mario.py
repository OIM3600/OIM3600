# for i in range(4):
#     print("🧱", end="")


"""
####
####
####
"""

# while True:
#     n = input("Size: ")
#     if n.isnumeric() and int(n) > 0:
#         n = int(n)
#         break

# for row_number in range(n):
#     for col_number in range(n):
#         print("🧱", end="")
#     print()


def get_size():
    """Ask user to enter an integer and return it"""
    while True:
        n = input("Size: ")
        if n.isnumeric() and int(n) > 0:
            n = int(n)
            return n


def build_wall(n):
    """Build n x n wall"""
    for row_number in range(n):
        for col_number in range(n):
            print("🧱", end="")
        print()


def main():
    size = get_size()
    build_wall(size)


main()
