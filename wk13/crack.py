import time
from string import digits, ascii_letters, punctuation
from itertools import product


def crack():
    """
    printing all the combinations of 4-digit passcode
    """
    # for i in digits:
    #     for j in digits:
    #         for k in digits:
    #             for l in digits:
    #                 print(i + j + k + l)
    for passcode in product(ascii_letters + digits + punctuation, repeat=8):
        print(passcode)


start = time.time()
crack()
end = time.time()
print(f"Time: {end - start}s")
