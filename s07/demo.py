# print("Hello, world!")
# # Correctness, Design, style
# name = input("What is your name? >> ")
# # print("Hello, ", answer, "!", sep="")
# print("Hello, " + name + "!")


# print(type(name))

# number = input("Please enter a number: ")
# number = int(number) # convert an "int-like" str to an int
# if number > 10:
#     print('The number is greater than 10.')
# else:
#     print('The number is not greater than 10.')

# Modify the code to ask for two numbers, and compare
# x = input("Please enter a number: ")
# x = int(x)

# y = int(input("Please enter another number: "))

# if x > y:
#     print("x > y")
# elif x == y:
#     print("x = y")
# else:
#     print("x < y")

# Example: simulate a login process, (ask for username and pswd)

# user = input("Enter your user name >> ")
# password = input("Enter your password >>")  # 123456

# if user == "admin" and password == "123456":
#     print("Welcome!")
# else:
#     print("Get out of here!")


# Loops

# counter = 3

# while counter > 0:
#     print("meow")
#     counter = counter - 1


# for i in range(3):
#     print("meow")


# while True:
#     print("meow")


# Keep asking user for password until he enters the right one

while True:
    password = input("Enter your password >> ")

    if password == "123456":
        print("Welcome!")
        break  # stop the loop
    else:
        print("Try one more time!")

# Ex. Keep track of # of trials


