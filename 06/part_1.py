races = []
with open("06/input.txt", "r") as file:
    lines = file.readlines()
    cols = list(map(lambda line: line.split(), lines))
    for i, col in enumerate(cols[0]):
        if col.isdigit():
            races.append([int(col), int(cols[1][i])])
prod = 1
for race in races:
    res = []
    for ms in range(race[0]):
        distance = ms * (race[0] - ms)
        if distance > race[1]:
            res.append(ms)
    prod = prod * len(res)

print(prod)
