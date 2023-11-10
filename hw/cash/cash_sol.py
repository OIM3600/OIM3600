def get_cents() -> int:
    """
    Ask how many cents the customer is owed, and return the number
    """
    while True:
        n = int(input('Change owed: '))
        if n > 0:
            return n


def calculate_quarters(cents: int) -> int:
    """
    Calculate the number of quarters to give the customer
    """
    return cents // 25


def calculate_dimes(cents: int) -> int:
    """
    Calculate the number of dimes to give the customer
    """
    return cents // 10


def calculate_nickels(cents: int) -> int:
    """
    Calculate the number of nickels to give the customer
    """
    return cents // 5


def calculate_pennies(cents: int) -> int:
    """
    Calculate the number of pennies to give the customer
    """
    return cents


def main():
    """
    You don't need to change any code in this function
    """
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25
    # print(cents)

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print the total number of coins to give the customer
    print(f"The total number of coins is {coins}.")


if __name__ == '__main__':
    main()
