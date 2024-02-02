print("hello, world!")

# try to change the code by
# removing ", (, ), ...
# changing function name
# " -> '

# answer = input("What is your name? >> ")
# print("Hello, " + answer + "!")  # + concatenation

# x = float(input("Enter value of x: "))
# y = float(input("Enter value of y: "))

# if x < y:
#     print("x is less than y.")
# elif x > y:
#     print("x is greater than y.")
# else:
#     print("x is equal to y.")


# age = input("How old are you? ")
# age = int(age)

# if age >= 21:
#     print("Yes, you can.")
# else:
#     print("Sorry, you cannot.")


# i = 0

# while i < 3:
#     print("meow")
#     i += 1

for i in range(3):
    print("meow")

print()

for i in range(5):
    print(i)


# 1 + 2 + 3 + 4 + 5 + ... + 10

# total = 0

# for i in range(11):
#     print(i)
#     total += i

# print("Sum = " + str(total))


# password login simulator

while True:
    password = input("Enter your password: ")

    if password == "123456":
        print("Welcome!")
        break
    else:
        print("Try again!")
