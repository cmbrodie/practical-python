# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    # expects lines to be of type list

    if select and has_headers == False and not silence_errors:
        raise RuntimeError("select argument requires column headers")
    # with open(filename) as f:
    #     rows = csv.reader(f, delimiter=delimiter)

    # Read the file headers
    # headers = next(rows) if has_headers else []
    lines = (
        [s.split(delimiter) for s in lines if type(s) == str]
        if (type(lines[0]) == str)
        else lines
    )
    headers = [l.strip() for l in lines[0]] if has_headers else []
    rows = lines[1:] if has_headers else lines

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    count = 0
    for row in rows:
        count += 1
        if not row:  # skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {count}: Couldn't convert", row)
                    print(f"Row {count}: Reason", e)

        # Make a dictionary
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records


def test():
    with open("Data/portfolio.csv") as f:
        file = csv.reader(f)
        port = parse_csv(list(file), types=[str, int, float])
    return port


port = test()
