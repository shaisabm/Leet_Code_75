import statistics

def findMaxAverage(nums, k: int):
  # if k == len(nums):
  #   return statistics.mean(nums)
  # sums = float('-inf')
  # index2 = k-1
  # index1 = 0
  # while index2 != len(nums):
  #   if sum(nums[index1:index2+1]) > sums:
  #     sums = sum(nums[index1:index2+1])
  #   nums.remove(nums[index1])
  # return sums/k
  
  # class Solution:
  #   def findMaxAverage(self, nums: List[int], k: int) -> float:
  #       currSum = maxSum = sum(nums[:k])

  #       for i in range(k, len(nums)):
  #           currSum += nums[i] - nums[i - k]

  #           maxSum = max(maxSum, currSum)

  #       return maxSum / k
  
nums, k = [5,2,2], 2

print(findMaxAverage(nums,k))
  
  
