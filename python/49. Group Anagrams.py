def groupAnagrams(strs):
  dic = {}
  for i in range(len(strs)):
      temp = list(strs[i])
      temp.sort()
      temp = ''.join(temp)
      if temp not in dic:
          dic[temp] = [strs[i]]
      else:
          dic[temp].append(strs[i])

  ans = list(dic.values())

  return ans




strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
