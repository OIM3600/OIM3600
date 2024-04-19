from itertools import product
from string import digits, ascii_letters, punctuation
import time


def crack():
    for i in digits:
        for j in digits:
            for k in digits:
                for l in digits:
                    passcode = i + j + k + l
                    print(passcode)


def crack_1():
    for passcode in product(digits, repeat=4):
        print(*passcode)


def crack_2():
    for passcode in product(ascii_letters, repeat=4):
        print(*passcode)


def crack_3():
    for passcode in product(digits + ascii_letters + punctuation, repeat=4):
        print(*passcode)


def main():
    start = time.time()
    # crack()
    # crack_1()
    # crack_2()
    crack_3()
    duration = time.time() - start
    print(f"time: {duration}s")


main()
