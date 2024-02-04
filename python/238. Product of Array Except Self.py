def productExceptSelf(nums):
  #ans = []
  # for i in range(0,len(nums)):
  #   product = 1
  #   for j in range(0,len(nums)):
  #     if j == i:
  #       continue
  #     else:
  #       product = product*nums[j]
  #   ans.append(product)
  # return ans
  left = [1]
  right = [0]*(len(nums)-1)
  for i in range(0,len(nums)-1):
    left.append(nums[i]*left[i])
  right.insert(len(right),1)
  right[len(right)-2] = nums[len(right)-1]

  count = len(nums) - 3
  while count != -1:
    right[count] = right[count+1] * nums[count+1]
    count -= 1  


  ans = []
  for x in range(0,len(right)):
    ans.append(right[x]*left[x])
  return ans  











nums = [3,4,6,1,2]

print(productExceptSelf(nums))