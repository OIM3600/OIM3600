prudential = 228  # Height (meters)
bill = 0.11 * 0.001  # Meters (0.11 mm)
num_bills = 1
day = 1

while num_bills * bill < prudential:
    print(day, num_bills, num_bills * bill)
    day = day + 1
    num_bills = num_bills * 2

print("Number of days:", day)
print("Number of bills:", num_bills)
print("Final height:", num_bills * bill)
