prices = {}

with open("Data/prices.csv", "rt") as f:
    for line in f:
        try:
            row = line.split(",")
            prices[row[0]] = float(row[1])
        except IndexError as i:
            print(i)
print(prices)
