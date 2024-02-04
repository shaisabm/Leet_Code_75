from typing import List
import math

def canPlaceFlowers(flowerbed: List[int], n: int):
  
  if (len(flowerbed) == 1 and flowerbed[0] == 0 and (n == 1 or n == 0)) or (len(flowerbed) == 1 and flowerbed[0] == 1 and n == 0):
      return True
  elif (len(flowerbed) == 1 and flowerbed[0] == 0 and n != 1) or (len(flowerbed) == 1 and flowerbed[0] == 1 and n != 0) or (n > math.ceil(len(flowerbed)/2)):
      return False

  count = 0
  for i in range(0,len(flowerbed)):
      if flowerbed[i] == 1:
          continue
      if i == 0 and flowerbed[i+1] == 0:
          count += 1
      elif i > 0 and i != len(flowerbed)-1:
          if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
              count += 1
              flowerbed[i] = 1
      elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
          count += 1
      if count >= n:
          return True
  return False







flowerbed = [0,0,0]
n = 2
print(canPlaceFlowers(flowerbed, n))
