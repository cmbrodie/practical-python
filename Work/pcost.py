# pcost.py
from stock import Stock
import report


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return sum([s.shares * s.price for s in portfolio])


def main(args):
    if len(args) != 2:
        print(f"please add a filename after {args[0]}")
        print(f"Total cost of portfolio.csv: {portfolio_cost('Data/portfolio.csv')}")
    else:
        filename = args[1]
        print("Total cost:", portfolio_cost(filename))


if __name__ == "__main__":
    import sys

    main(sys.argv)
