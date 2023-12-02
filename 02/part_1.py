import re
 
def isGameValid(gameData):
  return all(all(int(x) <= config[gameData.index(color)] for x in color) for color in gameData)

config = [12, 13, 14]
ttl = 0

with open("02/data/input.txt", "r") as file:
  data = list(map(lambda item: item.strip("\n"), file.readlines()))

games = list()
for line in data:
  id = re.search(r"(?<=Game\s)\d+", line).group()
  red = list(re.findall(r"\d+(?=\sred)", line))
  green = list(re.findall(r"\d+(?=\sgreen)", line))
  blue = list(re.findall(r"\d+(?=\sblue)", line))
  if isGameValid([red, green, blue]):
    ttl += int(id)

print(ttl)