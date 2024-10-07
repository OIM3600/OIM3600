def count_freq(s):
    """
    Calculates each item's frequency in a given string/list
    To represent the returned value, we could choose dict
    """
    freqs = {}  # initialize the variable to return

    # for loop over the string, check each letter
    #     if the letter has been seen before:
    #         set the value to the letter to 1
    #     else (which means we have seen the letter before, aka, the letter exists in the dict already)
    #         increment the value to the letter by 1
    for item in s:
        if item not in freqs:
            freqs[item] = 1
        else:
            freqs[item] += 1
    return freqs


def main():
    print(count_freq("babson"))  # {'b': 2, 'a': 1, 's':1, 'o': 1, 'n':1}
    doc = """
Understand the fundamental concepts of computer hardware and be able to identify and explain the functions of different hardware components.
Understand the principles of the Internet and be able to use web browsers and search engines effectively.
Understand the basics of programming and be able to create simple programs using Scratch.
Understand the principles of the Python programming language and be able to write simple programs using Python.
Understand basic algorithms and be able to design and implement simple algorithms to solve problems.
Understand the principles of web development and be able to create simple web pages using HTML, CSS, and JavaScript.
Understand the basics of SQL and be able to write simple queries to retrieve and manipulate data in a database.
Understand the principles of the Flask framework and be able to build simple web applications using Flask.
Understand the importance of cybersecurity and be able to implement basic security measures to protect computer systems and data.
Work effectively in a team to complete a final project that integrates and applies the knowledge and skills learned in the course.
"""
    words = doc.lower().replace(".", " ").split()
    # print(words)
    print(count_freq(words))


main()
