# pcost.py
#
# Exercise 1.27
import sys


def portfolio_cost(filename):
    """Takes in a filename and returns a total portfolio cost"""
    import csv

    tot = 0
    with open(filename, "rt") as p:
        lines = csv.reader(p)
        headers = next(lines)
        for line in lines:
            try:
                num_shares = int(line[1])
                price = float(line[2])
                tot += num_shares * price
            except ValueError:
                print(f"Couldn't parse line: {line}")

    return tot


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
cost = portfolio_cost(filename)
print(f"Total cost: ${cost}")
