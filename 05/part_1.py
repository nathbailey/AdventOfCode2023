import re


def getMappedValue(val, src, dest, len):
    srcMax = src + len
    if src <= val <= srcMax:
        return dest + (val - src)
    else:
        return val


with open("05/data/input.txt", "r") as file:
    data = file.read()

seeds = list(
    map(
        lambda number: int(number),
        re.search(r"(?<=seeds:\s)(\d+ ?)+", data).group().split(" "),
    )
)

keys = list(re.finditer(r"[a-z]+-to-([a-z]+)\smap:", data))
maps = {}
for i, res in enumerate(keys):
    if i + 1 < len(keys):
        end = keys[i + 1].start() - 1
    else:
        end = len(data)
    maps[res.group(1)] = list(
        map(
            lambda item: list(map(lambda number: int(number), item.split(" "))),
            re.search(r"((\d+ ?)+\n)+(\d+ ?)+", data[(res.end() + 1) : end])
            .group()
            .split("\n"),
        )
    )

locations = []
for seed in seeds:
    prev = seed
    for map in maps:
        for mapItem in maps[map]:
            res = getMappedValue(prev, mapItem[1], mapItem[0], mapItem[2])
            if res != prev:
                break
        prev = res
    locations.append(res)

locations.sort()

print(locations[0])
