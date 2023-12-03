import re

with open("03/data/input.txt", "r") as file:
  data = list(map(lambda item: item.strip("\n"), file.readlines()))

symbols = {}
gears = {}
total = 0

for row in range(len(data[0]) - 1):
    for col in range(len(data)):
        if data[row][col] not in '0123456789.':
            symbols[(row, col)] = data[row][col]
            if data[row][col] == "*":
                gears[(row, col)] = []

for rowNum, row in enumerate(data):
    for col in re.finditer(r'\d+', row):
        possibilities = []
        for i in range(col.start() - 1, col.end() + 1):
            possibilities.append((rowNum - 1, i))
            possibilities.append((rowNum, i))
            possibilities.append((rowNum + 1, i))
        for p in possibilities:
            if p in symbols:
                if p in gears:
                    gears[p].append(int(col.group()))

for gear in gears:
    if len(gears[gear]) == 2:
        total += (gears[gear][0] * gears[gear][1])

print(total)