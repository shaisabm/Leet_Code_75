import math
def gcdOfStrings(str1, str2):

  if str1 == str2: return str1
  elif str1 not in str2 and str2 not in str1: return ""


  len_str1 = len(str1)
  len_str2 = len(str2)

  # def cf(len_str1, len_str2):
  #   common_div =[]

  #   if len_str1 <= len_str2:
  #     for i in range (1, len_str1+1):
  #       if len_str2%i == 0:
  #         common_div.append(i)
  #   else:
  #     for j in range (1, len_str2+1):
  #       if len_str1%j == 0:
  #         common_div.append(j)
  #   return common_div

  # print(cf(len_str1, len_str2))
  diff = math.fabs(len_str1 - len_str2)
  ans = []
  if len_str1 < len_str2:
    for i in str2:
      if i not in str1:
        return ""
    x = len_str2 - 1
    y = 0
    while y < diff:
      ans.append(str2[x])
      y += 1
      x -= 1
  else:
    for j in str1:
      if j not in str2:
        return ""
    x = len_str2 - 1
    y = 0
    while y < diff:
      ans.append(str1[x])
      y += 1
      x -= 1

  ans.reverse()
  return ''.join(ans)








str1 = "ABC"
str2 = "ABCDEF"
x = gcdOfStrings(str1, str2)
print(x)
