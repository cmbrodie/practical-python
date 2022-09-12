# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):

    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            record["shares"] = int(record["shares"])
            record["price"] = float(record["price"])
            portfolio.append(record)

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


def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        n = row["name"]
        s = row["shares"]
        p = prices[row["name"]]
        c = prices[row["name"]] - row["price"]
        report.append((n, s, p, c))

    return report


def main():
    report = make_report(
        read_portfolio("Data/portfolio.csv"), read_prices("Data/prices.csv")
    )
    headers = ("Name", "Shares", "Price", "Change")
    n, s, p, c = headers
    print(f"{n:>10s} {s:>10s} {p:>10s} {c:>10s}")
    print(f"{'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s}")
    for n, s, p, c in report:
        p = f"${p:.2f}"
        print(f"{n:>10s} {s:>10d} {p:>10s} {c:>10.2f}")


if __name__ == "__main__":
    main()

f = open("Data/dowstocks.csv")
types = [str, float, str, str, float, float, float, float, int]
rows = csv.reader(f)
headers = next(rows)
dowstocks = [
    {name: func(val) for name, func, val in zip(headers, types, row)} for row in rows
]
for stock in dowstocks:
    stock["date"] = tuple(int(i) for i in stock["date"].split("/"))
