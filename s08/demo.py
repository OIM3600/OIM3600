# a = int(input('Enter an integer: '))

# if a % 2:
#     print('It is an odd number.')
# else:
#     print('It is an even number.')


# Wrap the code into function which is to check whether a year is a leap year


def get_year():
    """
    Get input from user, return a valid year
    """
    year = int(input("Enter a year: "))
    return year


def check(year):
    """
    Checks whether year is a leap year, prints the result

    (Parameters): year, which is an integer
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")


check(get_year())
