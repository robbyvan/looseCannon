class Solution(object):
  def isScramble(self, s1, s2):
    n, m = len(s1), len(s2)
    if n != m or sorted(s1) != sorted(s2):
      return False
    if n < 4 or s1 == s2:
      return True

    for cut in range(1, n):
      if self.isScramble(s1[:cut], s2[:cut]) and self.isScramble(s1[cut:], s2[cut:]):
        return True
      if self.isScramble(s1[:cut], s2[-cut:]) and self.isScramble(s1[cut:], s2[:-cut]):
        return True
    return False