from collections import Counter

with open("07/input.txt", "r") as file:
    data = file.read().splitlines()

ans = sum(
    (rank + 1) * bid
    for rank, (*_, bid) in enumerate(
        sorted(
            (
                max(0, 0, *map(hand.count, set(hand) - {"J"})) + hand.count("J"),
                -(max(1, len(set(hand) - {"J"}))),
                *map("J23456789TQKA".index, hand),
                int(str_bid),
            )
            for hand, str_bid in map(str.split, data)
        )
    )
)

print(ans)
