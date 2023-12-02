import re

with open("01/data/input.txt", "r") as file:
  data = list(map(lambda item: item.strip("\n"), file.readlines()))

total = 0
for i, item in enumerate(data):
  nums = re.findall(r'\d', item)
  num = nums[0] + nums[len(nums) - 1]
  total += int(num)

print(total)