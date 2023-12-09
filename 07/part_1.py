from collections import Counter
from pathlib import Path

with open("07/input.txt", "r") as file:
    data = file.read().splitlines()

ans = sum(
    (rank + 1) * bid
    for rank, (*_, bid) in enumerate(
        sorted(
            (
                max(Counter(hand).values()) - len(set(hand)),
                *map("23456789TJQKA".index, hand),
                int(str_bid),
            )
            for hand, str_bid in map(str.split, data)
        )
    )
)

print(ans)
