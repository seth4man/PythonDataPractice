# Exercise focused on space efficiency in large file

class dataClass:
    def __init__(self, route, date, dayType, numRides):
        self.route = route
        self.date = date
        self.dayType = dayType
        self.numRides = numRides


def read_data(filename):
    data = []
    with open(filename) as file:
        headers = next(file)
        for line in file:
            record = make_record(line)
            data.append(record)
    return data

def make_record(line):
    # What is the most memory efficient way to represent a row of data
    # Amount of memory used with various data structures to read and store 15MB file:
    # String: 52.1712275 MB
    # List: 170.70362980000002 MB
    # Dict: 266.1365073 MB
    # Tuple: 159.9975786 MB
    # Class: 213.1204449 MB

    # line = list(line.split(','))
    line = tuple(line.split(','))
    line = dataClass(line[0], line[1], line[2], line[3])
    # line = {
    #     'route': line[0],
    #     'date': line[1],
    #     'dayType': line[2],
    #     'numRides': line[3]
    # }

    return line

# Using this code to test memory usage of different data structures
import tracemalloc
total = 0
for x in range(9):
    tracemalloc.start()
    data = read_data('ctabus.csv')
    total += tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
average = total/10
averageMB = average/1000000
print(averageMB, 'MB')