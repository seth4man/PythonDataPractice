# Find a way to read in 'ctabus.csv' that makes Python
# much more memory efficient than seen in 'CTABus.py'

#Place each column into a list
#Memory used: 128.8688209 MB (Better than storing in tuples)
#Memory used when also using library for storing dates: 110.97282179999999 MB
import datetime
def read_data(filename):
    route = []
    date = []
    dayType = []
    numRides = []
    with open(filename) as file:
        headers = next(file)
        for line in file:
            line = list(line.split(','))
            route.append(line[0])
            mon, day, year = line[1].split('/')
            date.append(datetime.date(int(year), int(mon), int(day)))
            dayType.append(line[2])
            numRides.append(line[3])
    return (route, date, dayType, numRides)

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