class Solution(object):
  def romanToInt(self, s):
    roman = { 'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D': 500 }
    z = 0
    for i in xrange(0, len(s) - 1):
      if roman[s[i]] < roman[s[i + 1]]:
        z -= roman[s[i]]
      else:
        z += roman[s[i]]
    return z + roman[s[-1]]