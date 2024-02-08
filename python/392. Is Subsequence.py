def isSubsequence(s: str, t: str):
  count = 0
  index = 0
  
  for i in range(len(t)):
    if s[index] == t[i]:
      count += 1
      index += 1
    if count == len(s):
      return True
  return False


s = ""
t = "c"
print(isSubsequence(s,t))