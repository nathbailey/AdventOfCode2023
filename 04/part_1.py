import re

with open("04/data/input.txt", "r") as file:
    data = list(map(lambda line: line.strip("\n") , file.readlines()))

total = 0
for card in data:
    sanitized = card.split(":")[1]
    winning = list(re.findall(r"\d+", sanitized.split("|")[0]))
    have = list(re.findall(r"\d+", sanitized.split("|")[1]))
    matches = []
    for w in winning:
        if w in have:
            matches.append(w)
    points = 0
    if len(matches) > 0:
      points = 1
      for m in range(0, len(matches) - 1):
          points *= 2
    total += points
  
print(total)