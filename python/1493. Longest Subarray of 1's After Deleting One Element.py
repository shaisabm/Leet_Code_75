

def longestSubarray(nums):
  k = 1
  left = 0
  max_len = 0
  
  for right in range(len(nums)):
    if nums[right] == 0:
      k -= 1
      
    if k < 0:
      if nums[left] == 0:
        k +=1
      left+= 1
  return right - left



nums = [0,1,1,1,0,1,1,0,1]

print(longestSubarray(nums))


# def longestSubarray(nums, k = 1):
# left = 0
# zero_counter = 0
# max_len = 0
# for right in range(len(nums)):

#   if nums[right] == 0:
#     zero_counter += 1


#   while zero_counter > k:
#     if nums[left] == 0:
#       zero_counter -= 1
#     left += 1
#   curr_len = right+1 - left
#   max_len = max(curr_len, max_len)
# return max_len-1