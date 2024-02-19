
def findMaxAverage(nums, k: int):
  
  if k == len(nums): return sum(nums)/k
  currSum = sum(nums[:k])
  m = currSum
  sums = []
  for i in range(k,len(nums)):
      currSum = currSum - nums[i-k] + nums[i]
      m = max(currSum, m)
  return m/k
    
    
  
nums, k = [1,12,-5,-6,50,3], 5

print(findMaxAverage(nums,k))
  
  
