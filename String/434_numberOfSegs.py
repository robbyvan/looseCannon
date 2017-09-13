class Solution(object):
  def countSegments(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
      return 0
    p, counter = 0, 0
    while p < len(s):
      while p < len(s) and s[p] == ' ':
        p += 1
      if p < len(s):
        counter += 1
      while p < len(s) and s[p] != ' ':
        p += 1
    return counter
