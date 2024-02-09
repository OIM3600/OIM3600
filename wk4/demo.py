# import alex

# alex.say()


# a = 10


# def f():
#     # global a
#     a = 3
#     print(a * 2)


# f()

# print(a)


def is_leap(year):
    """check if the given year is a leap year"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# is_leap(2000)
# is_leap(2024)
# is_leap(2025)
# is_leap(2100)


a = 10
a + 5  # this is an expression, which does not have any effect


print(a + 5)  # this is a statement, which has effect


print("Hello,", end="\n")
print("world!")


print("hi", "world", sep="...")


# score = 95

# if score >= 60:
#     print("pass")

# if score >= 90:
#     print("A")
# else:
#     print("fail")


def check(score):
    if score >= 60:
        print("pass")
        return 1  # return immediately ends the function

    if score >= 90:
        print("A")
        return 2
    else:
        print("fail")
        return 0


res = check(59)
print(res)
