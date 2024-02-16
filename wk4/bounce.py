# - initialize height and number of bounces
# - Repeat the following as long as number of bounces is less than or equal to 10
#   - calcuate the new height
#   - print as required, i, height
#   - increase the number of bounces

height = 100
i = 1

while i <= 10:
    height = height * 0.6
    print(f"{i}: {height:.2f}")
    i += 1


# Try to use for loop to do this

height = 100

for i in range(10):
    height *= 0.6
    print(f"{i+1}: {height:.3f}")
