class Solution(object):
  def minWindow(self, s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, char in enumerate(s, 1):
      if need[char] > 0:
        missing -= 1
      need[char] -= 1

      if not missing:
        while i < j and need[s[i]] < 0:
          need[s[i]] += 1
          i += 1
        if J == 0 or j - i <= J - I:
          I, J = i, j
    return s[I:J]
