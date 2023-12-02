import re

def numStringToValue(v: str):
  switcher = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
  }
  return str(switcher.get(v, v))

with open("01/data/input.txt", "r") as file:
  data = list(map(lambda item: item.strip("\n"), file.readlines()))

total = 0
for i, item in enumerate(data):
  nums = list(map(lambda res: numStringToValue(res), re.findall(r'\d|zero|one|two|three|four|five|six|seven|eight|nine', item)))
  num = nums[0] + nums[len(nums) - 1]
  total += int(num)

print(total)