from typing import List
import copy
def compress(chars: List[str]):
  s = copy.deepcopy(chars)
  chars.clear()
  i = 0
  
  while i < len(s): 
    count = 0
    chars.append(s[i])

    front = s[i]
    x = i
    try:
      while front == s[x]:
        count +=1
        x+=1
    except IndexError:
        pass

    if count != 1:
      str(count)
      for i in range(0,len(str(count))):
        chars.append(str(count)[i])
    i = x
  return len(chars)









chars = ["a","a","a","a","a","a","a","a","a","a","b","b","c","c","c"]


print(compress(chars))