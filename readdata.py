# Read file "portfolio.csv" into a Python List.

def read_portfolio(filename):
    portfolio = []  #instantiate list

    with open(filename) as file:
        next(file)  # discard first line
        for line in file:
            parts = line.split(',')
            record = {
                'name': parts[0][1:-1],     #Strip quotation marks
                'shares': int(parts[1]),
                'price': float(parts[2])
            }
            portfolio.append(record)

    return portfolio