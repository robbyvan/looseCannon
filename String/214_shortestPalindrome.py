class Solution(object):
  def shortestPalindrome(self, s):
    if self.isPalindrome(s):
      return s

    longest = 1
    for end in xrange(1, len(s)):
      if self.isPalindrome(s[:end]):
        longest = end

    return s[longest:][::-1] + s

  def isPalindrome(self, s):
    if len(s) < 2:
      return True
    start, end = 0, len(s) - 1
    while start < end:
      if s[start] != s[end]:
        return False
      start, end = start + 1, end - 1
    return True

class Solution(object):
  def shortestPalindrome(self, s):
    r = s[::-1]
    for i in range(len(s) + 1):
      if s.startswith(r[i:]):
        return r[:i] + s