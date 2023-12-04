import re

def getWonCards(card):
    cardNo, sanitized = card.split(":")
    cardNo = re.search(r"\d+", cardNo).group()
    winning = list(re.findall(r"\d+", sanitized.split("|")[0]))
    have = list(re.findall(r"\d+", sanitized.split("|")[1]))
    matches = 0
    cards = []
    for w in winning:
        if w in have:
            matches += 1
            cards.append(int(cardNo) + matches)
            cards.extend(getWonCards(data[int(cardNo) + matches - 1]))
    return cards

with open("04/data/input.txt", "r") as file:
    data = list(map(lambda line: line.strip("\n") , file.readlines()))

total = 0
for line in data:
    total += 1
    total += len(getWonCards(line))

print(total)