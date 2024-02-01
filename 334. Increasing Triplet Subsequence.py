from typing import List
def increasingTriplet(nums:List[int]):

  return any(left(nums, i) and right(nums, i) == True for i in range(1, len(nums)))


def left(nums, index) -> bool:
  return any(nums[i] < nums[index] for i in range(0,index))

def right(nums, index) -> bool:
  return any(nums[i] > nums[index] for i in range(index, len(nums)))










nums = [20,100,10,0,0,0,0,0,12,5, 12,13]
# print(left(nums, 4))
# print(right(nums, 4))
print(increasingTriplet(nums))