# n = 5
# while n > 0:
#     print(n)
#     n = n - 2

# print("after while loop,", n)

# for i in range(6, 0, -2):
#     print(i)

# print("after for loop,", i)


# Use for loop
# when you know the exact number of iterations
# for _ in range(3):
#     print("meow!")

# when you know the range of an integer sequence

# for i in range(-10, 11, 2):
#     print(i**2)

# when you need to iterate over a collection/sequence, such as a string, list, tuple, dictionary, set ...

# for letter in "alex":  # a string
#     print(letter.upper())

# for num in [18, 324, 5234, 643]:  # a list
#     print(num**2)

# for num in (18, 324, 5234, 643):  # a tuple
#     print(num**2)

# d = {"jeff": 90, "alex": 91}

# for k in d.keys():  # iterate over a dict's keys
#     print(k)
#     print(d[k])

# for v in d.values(): # iterate over a dict's values
#     print(v)

# for k, v in d.items():  # iterate over a dict's keys and values
#     print(k, v)

# Use while loop
# when you need to create an infinite loop

# while True:
#     # game()
#     start_server()

# when you don't know the exact number of iterations beforehand, and want to continue until
# ... the specific condition is no longer true

# user_input = input("Please enter your password: ")
# while user_input != "123456":
#     print("wrong password")
#     user_input = input("Try again: ")

# or until a break statement is encountered

# while True:
#     user_input = input("Please enter your password: ")
#     if user_input == "123456":
#         print("You are logged in. Welcome!")
#         break
#     else:
#         print("Wrong password. Try again!")
