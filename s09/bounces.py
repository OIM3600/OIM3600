# height = 100
# ratio = 0.6
# n = 0  # keeps track of times

# # print the table showing all the bounces
# # epsilon = 0.00000001
# # while height > epsilon:
# #     print(n, height)
# #     height = height * ratio
# #     n += 1

# # print the table showing first 10 bounces
# times = 10
# while n < times:
#     height *= ratio
#     n += 1
#     print(n, height)

# print()


# # print the same table using for loop
# height = 100
# for i in range(times):
#     height *= ratio
#     print(i + 1, height)


def print_bounces_while(height, ratio, times):
    """
    prints the table showing first 10 bounces
    """
    n = 0  # keeps track of times
    while n < times:
        height *= ratio
        n += 1
        print(n, height)


def print_bounces_for(height, ratio, times):
    """
    prints the same table using for loop
    """
    for i in range(times):
        height *= ratio
        print(i + 1, height)


def main():
    height = 100
    ratio = 0.6
    times = 10
    print_bounces_while(height, ratio, times)
    print()
    print_bounces_for(height, ratio, times)


main()
