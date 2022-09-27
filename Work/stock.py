class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt

    def __repr__(self):
        price = f"${self.price:.2f}"
        return f"name: {self.name} shares: {self.shares} price: {price}"


def main():
    a = Stock("GOOG", 100, 49.01)
    b = Stock("AAPL", 50, 122.34)
    c = Stock("IBM", 75, 91.75)
    b.shares * b.price
    6117.0
    c.shares * c.price
    6881.25
    stocks = [a, b, c]
    for s in stocks:
        print(s)
        print(f"Total cost of {s.name} is ${s.cost():.2f}\n")

    import fileparse

    with open("Data/portfolio.csv") as lines:
        portdicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )
    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
    print(portfolio)


if __name__ == "__main__":
    main()
