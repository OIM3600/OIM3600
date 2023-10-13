import time


# def draw(n):
#     print('#' * n)
#     time.sleep(0.5)
#     draw(n + 1)  # recursion


def draw(n):
    if n <= 0:
        return
    draw(n - 1)
    print('#' * n)
    time.sleep(0.5)


def main():
    draw(4)


main()
