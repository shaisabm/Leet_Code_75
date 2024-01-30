def reverseWords(s: str):
  s2 = ((s.rstrip()).split())[::-1]
  return ' '.join(s2)


s = "the sky is blue"

print(reverseWords(s))