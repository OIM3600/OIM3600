while True:
    height = input('Height: ')
    height = int(height)
    if 1 <= height <= 8:
        break

# print(height)

# Nested for loops
# for i in range(height):
#     print(i + 1)
#     for j in range(i + 1):
#         print('#', end='')

#     print()

for i in range(height):
    print('#' * (i + 1))
