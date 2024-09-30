# def f(x):
#     print(x * 2) # side effect of the function
#     # if there is no return statement, the function will automatically return None
#     # return None


# result = f(100)
# print(result)


# x = 100 # global variable

# def f():
#     x = 42  # local variable
#     return x * 2

# print(x, f())

# n = 5
# while n != 0:
#     print(n)
#     n = n - 2


# - Use a for loop
# - when the number of iterations is known in advance.
for i in range(4):
    print("Hello")
# - when iterating over a specific range of integers.
for i in range(10, 15):
    print(i)

# - when looping through elements in a collection or sequence (e.g., string, list, tuple, dictionary, set)
for c in "Amelia123":
    print(c.upper())

for num in [9, 30, 2024]:
    print(num**2)

# - Use a while loop
# - when creating an infinite loop.
# while True:
# game()
# start_server()

# - when the number of iterations is unknown and should continue until:
# - a specific condition becomes False.

# the bounce case (printing all the bounces)
password = input("Password: ")
while password != "123456":
    print("Please enter again.")
    password = input("Password: ")

# - or a break statement is encountered.
while True:
    password = input("Password: ")
    if password == "123456":
        break
    else:
        print("Please enter again.")
