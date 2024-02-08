
def moveZeroes(nums) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  count = nums.count(0)
  for i in range(count):
      nums.append(nums[nums.index(0)])
      nums.remove(0)


  print(nums)


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)