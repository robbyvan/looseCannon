class Solution(object):
  def reverseString(self, s):
    """
    @param s: String
    @return: String
    """
    ls = list(s)
    i, j = 0, len(ls) - 1
    while i < j:
      ls[i], ls[j] = ls[j], ls[i]
      i += 1
      j -= 1
    return ''.join(ls)

# return s[::-1]