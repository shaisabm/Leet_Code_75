
def maxArea(height):
  lastIndex = len(height)-1
  maxArea = -1
  firstIndex = 0

  while firstIndex <= lastIndex:
    currentArea = (lastIndex-firstIndex)*min(height[lastIndex], height[firstIndex])

    if maxArea < currentArea:
      maxArea = currentArea

    if height[firstIndex] < height[lastIndex]:
        firstIndex += 1
    else: lastIndex -= 1


  return maxArea










height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))