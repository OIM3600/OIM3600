# for i in range(4):
#     print("?", end="")

# print('\n')

# for i in range(3):
#     print("#")

# ask user to enter the number of bricks, then print the brick row


# # Get the size from user
# while True:
#     n = input("Enter the size: ")
#     n = int(n)
#     # if n > 0 and n <= 8:
#     if 0 < n <= 8:
#         break
#     else:
#         print("Try again.")


# # Build a n x n wall
# for i in range(n):  # repeat the following task n times
#     # The following 3 lines are doing one job: creating one row of n bricks
#     for j in range(n):
#         print("🧱", end="")
#     print()


# Get the size from user
def get_size():
    """
    Gets the size of the wall, returns the size
    """
    while True:
        n = input("Enter the size: ")
        n = int(n)
        # if n > 0 and n <= 8:
        if 0 < n <= 8:
            return n
        else:
            print("Try again.")


# Build a n x n wall
def build_wall(n):
    """
    Prints a n x n wall.
    """
    for i in range(n):  # repeat the following task n times
        # The following 3 lines are doing one job: creating one row of n bricks
        for j in range(n):
            print("🧱", end="")
        print()


def main():
    size = get_size()
    build_wall(size)


main()
