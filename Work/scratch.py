portfolio = [
    ("GOOG", 100, 490.1),
    ("IBM", 50, 91.1),
    ("CAT", 150, 83.44),
    ("IBM", 100, 45.23),
    ("GOOG", 75, 572.45),
    ("AA", 50, 23.15),
]

from collections import Counter, defaultdict

total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

print(total_shares["IBM"])


holdings = defaultdict(list)

for name, shares, price in portfolio:
    holdings[name].append((shares, price))

print(holdings["IBM"])


def read_prices(filename: str) -> dict:
    """
    Read prices from a CSV file of name, price data
    """
    import csv

    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        try:
            for row in f_csv:
                prices[row[0]] = float(row[1])
        except IndexError:
            pass
        return prices


prices = read_prices("Data/prices.csv")


def divide(a, b):
    q = a // b
    r = a % b
    return q, r
