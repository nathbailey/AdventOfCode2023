with open("06/input.txt", "r") as file:
    lines = file.readlines()
    race = list(
        map(lambda line: int(line.strip("\n").replace(" ", "").split(":")[1]), lines)
    )

res = 0
for ms in range(race[0]):
    distance = ms * (race[0] - ms)
    if distance > race[1]:
        res += 1

print(res)
