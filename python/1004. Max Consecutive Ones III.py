

def longestOnes(nums, k):
  left = 0
  zero_counter = 0
  max_len = 0
  for right in range(len(nums)):

    if nums[right] == 0:
      zero_counter += 1


    while zero_counter > k:
      if nums[left] == 0:
        zero_counter -= 1
      left += 1
    curr_len = right+1 - left
    max_len = max(curr_len, max_len)
  return max_len



nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]

k = 3
print(longestOnes(nums, k))