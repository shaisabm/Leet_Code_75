
def mergeAlternately(word1, word2):
  x = 0
  w1 = 0
  w2 = 0
  marged = []
  while x < len(word1) or x < len(word2):

    if w1 < len(word1):
      marged.append(word1[w1])
      w1 += 1
    if w2 < len(word2):
      marged.append(word2[w2])
      w2 += 1
    x += 1
    return marged










word1 = ""
word2 = ""
mergeAlternately(word1, word2)