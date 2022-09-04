# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):

    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {}
            holding["name"] = row[0]
            holding["shares"] = int(row[1])
            holding["price"] = float(row[2])
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    d = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                d[row[0]] = float(row[1])
            except:
                print()

    return d


def net_gain(portfolio, prices):
    total = 0
    for row in portfolio:
        total += row["shares"] * (prices[row["name"]] - row["price"])
    return total


def main():
    val = net_gain(read_portfolio("Data/portfolio.csv"), read_prices("Data/prices.csv"))
    print(f"your net portfolio value change is: {val}")


if __name__ == "__main__":
    main()
