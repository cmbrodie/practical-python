# report.py
#
# Exercise 2.4
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    return parse_csv(
        filename=filename, select=["name", "shares", "price"], types=[str, int, float]
    )


def read_prices(filename):
    return dict(parse_csv(filename=filename, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        n = row["name"]
        s = row["shares"]
        p = prices[row["name"]]
        c = prices[row["name"]] - row["price"]
        report.append((n, s, p, c))

    return report


def print_report(report):
    """print headers"""
    headers = ("Name", "Shares", "Price", "Change")
    n, s, p, c = headers
    print(f"{n:>10s} {s:>10s} {p:>10s} {c:>10s}")
    print(f"{'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s}")
    """print report"""
    for n, s, p, c in report:
        p = f"${p:.2f}"
        print(f"{n:>10s} {s:>10d} {p:>10s} {c:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


"""Interesting code Uncomment"""

# f = open("Data/dowstocks.csv")
# types = [str, float, str, str, float, float, float, float, int]
# rows = csv.reader(f)
# headers = next(rows)
# dowstocks = [
#     {name: func(val) for name, func, val in zip(headers, types, row)} for row in rows
# ]
# for stock in dowstocks:
#     stock["date"] = tuple(int(i) for i in stock["date"].split("/"))


"""old code, changed in section 3.4 (modularized)"""
# def read_portfolio(filename):
#     """
#     Read a stock portfolio file into a list of dictionaries with keys
#     name, shares, and price.
#     """
#     portfolio = []
#     with open(filename, "rt") as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             record = dict(zip(headers, row))
#             record["shares"] = int(record["shares"])
#             record["price"] = float(record["price"])
#             portfolio.append(record)

#     return portfolio


# def read_prices(filename):
#     d = {}
#     with open(filename, "rt") as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 d[row[0]] = float(row[1])
#             except:
#                 ...

#     return d
