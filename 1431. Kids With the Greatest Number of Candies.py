from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int):
  max_candies = max(candies)
  boolen = []
  for i in candies:
    if i+extraCandies >= max_candies:
      boolen.append(True)
    else:
      boolen.append(False)
  return boolen


candies = [3]
extraCandies = 2
print(kidsWithCandies(candies,extraCandies))