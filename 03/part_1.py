import re

with open("03/data/input.txt", "r") as file:
  data = list(map(lambda item: item.strip("\n"), file.readlines()))

symbols = {}
total = 0

for row in range(len(data[0]) - 1):
    for col in range(len(data)):
        if data[row][col] not in '0123456789.':
            symbols[(row, col)] = data[row][col]

for rowNum, row in enumerate(data):
    for col in re.finditer(r'\d+', row):
        possibilities = []
        for i in range(col.start() - 1, col.end() + 1):
            possibilities.append((rowNum - 1, i))
            possibilities.append((rowNum, i))
            possibilities.append((rowNum + 1, i))
        valid = False
        for p in possibilities:
            if p in symbols:
                valid = True
        if valid:
            total += int(col.group())

print(total)