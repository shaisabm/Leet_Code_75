
def reverseVowels(s: str):
  index = []
  vowels = ["a", "e", "i", "o", "u"]
  for i in range(len(s)):
    if s[i] in vowels:
      index.append(i)

  original = index.copy()
  index.reverse()

  string = list(s)
  x = 0
  for i in original:
    string[i] = s[index[x]]
    x += 1
  return ''.join(string)





s = "leetcode"
print(reverseVowels(s))

