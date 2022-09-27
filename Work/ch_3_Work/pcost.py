# pcost.py
#
# Exercise 1.27

import sys

import report


def portfolio_cost(filename):
    """Takes in a filename and returns a total portfolio cost"""
    return sum(
        [
            row["shares"] * row["price"]
            for row in report.read_portfolio(filename=filename)
        ]
    )


def main(arglist=sys.argv):

    if len(arglist) == 2:
        filename = arglist[1]
    else:
        filename = "Data/portfoliodate.csv"
        print(f"please add a csv file after {sys.argv[0]}")
    cost = portfolio_cost(filename)
    print(f"Total cost: ${cost}")


if __name__ == "__main__":
    main()

# def portfolio_cost(filename):
#     """Takes in a filename and returns a total portfolio cost"""
#     import csv

#     tot = 0
#     with open(filename, "rt") as p:
#         rows = csv.reader(p)
#         headers = next(rows)
#         for rowno, row in enumerate(rows, start=1):
#             record = dict(zip(headers, row))
#             try:
#                 num_shares = int(record["shares"])
#                 price = float(record["price"])
#                 tot += num_shares * price
#                 print(record)
#             except ValueError:
#                 print(f"Row {rowno} Bad row: {row}")

#     return tot
