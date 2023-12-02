import re

ttl = 0

with open("02/data/input.txt", "r") as file:
  data = list(map(lambda item: item.strip("\n"), file.readlines()))

games = list()
for line in data:
  id = re.search(r"(?<=Game\s)\d+", line).group()
  red = max(list(map(lambda i: int(i), re.findall(r"\d+(?=\sred)", line))))
  green = max(list(map(lambda i: int(i), re.findall(r"\d+(?=\sgreen)", line))))
  blue = max(list(map(lambda i: int(i), re.findall(r"\d+(?=\sblue)", line))))
  power = red * green * blue
  ttl += power

print(ttl)