
def maxVowels(s,k):
  # Sliding Window

  vowels = {'a','e','i','o','u'}
  left = 0
  right = k-1
  count = 0
  subsing = list(s[left:right+1])

  for i in vowels:
    count += subsing.count(i)


  curr = count
  right += 1
  while right < len(s):
    if s[left] in vowels:
      curr -= 1
    if s[right] in vowels:
      curr += 1
    if curr == k: return curr
    count = max(curr, count)
    right += 1
    left += 1

  print(count)
  



s = "abciiidef"
k = 3
print(maxVowels(s,k))
