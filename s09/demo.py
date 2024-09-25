# height = 228  # this is a statement, which has some effect

# # print(height)

# height * 2 # this is an expression, which has a type and a value


# print(height)


score = 95


def check_grade(score):
    if score > 60:
        # print("Pass")
        return "Pass" # return will immediately end the function
    if score > 90:
        # print("A")
        return "A"
    else:
        # print("Fail")
        return "Fail"


grade = check_grade(score)
print(grade)
