def get_total_cost():
    """"""
    with open("data/portfolio.csv", "r") as file:
        # initialize total = 0
        stock_list = []
        total = 0
        for i, line in enumerate(file):
            print(line.strip())
            # check this line,
            # if it is the first line
            #    skip
            # else:
            # get shares and price by spliting by ','
            # add shares*price to total
            if i == 0:
                continue
            s = line.strip("\n").split(",")
            name = s[0]
            share = int(s[1])
            price = float(s[2])
            stock_list.append([name, share, price])
            total += share * price

        print(f"Total cost: ${total:.2f}")
        print(stock_list)


get_total_cost()
