def read_data(filename):
    """return the data from the file"""
    with open(filename, 'r') as f:
        data = f.readlines()
        # print(type(data))
        return data


def print_data(data):
    """print the data in a nice format"""
    total = 0

    for i, line in enumerate(data):
        line = line.strip()
        name, share, price = line.split(',')
        if i == 0:  # it is the header
            print(f'{name:5}{share:>10}{price:>10}')
        else:
            share = int(share)
            price = float(price)
            print(f'{name:5}{share:10d}{price:10.2f}')
            total += share * price

    print(f'Total cost: ${total}')


def main():
    data = read_data('data/portfolio.csv')
    # print(data)
    print_data(data)


main()
