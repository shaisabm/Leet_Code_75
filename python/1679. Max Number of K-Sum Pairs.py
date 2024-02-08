
from typing import Counter


def maxOperations(nums, k:int):
  operations = 0
  newNums = lambda nums, k: [x for x in nums if (x < k)]
  newNums = newNums(nums,k)
  newNums.sort()
  left = 0
  right = len(newNums)-1
  
  while left < right:
    if newNums[left] + newNums[right] < k:
      left += 1
    elif newNums[left] + newNums[right] > k:
      right -=1
    else:
      operations += 1
      left+=1
      right -= 1
  return operations
    


  

nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]



k = 2
maxOperations(nums,k)