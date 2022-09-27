# report.py

from stock import Stock

import fileparse
import tableformat


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )
    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    # print("%10s %10s %10s %10s" % headers)
    # print(("-" * 10 + " ") * len(headers))
    # for row in reportdata:
    #     print("%10s %10d %10.2f %10.2f" % row)
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, format="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    if format == "txt":
        formatter = tableformat.TextTableFormatter()
    elif format == "html":
        formatter = tableformat.HTMLTableFormatter()
    elif format == "csv":
        formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        print("please add cl args after filename")
        portfolio_report("Data/portfolio.csv", "Data/prices.csv")
    else:
        portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    import sys

    main(sys.argv)
