def calc():
    """
    Calculates how many days it takes ..., prints the results
    """
    bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
    prudential_height = 228  # Height (meters)
    num_bills = 1
    day = 1

    while num_bills * bill_thickness < prudential_height:
        print(day, num_bills, num_bills * bill_thickness)
        day = day + 1
        num_bills = num_bills * 2

    print("Number of days:", day)
    print("Number of bills:", num_bills)
    print("Final height:", num_bills * bill_thickness)


calc()
