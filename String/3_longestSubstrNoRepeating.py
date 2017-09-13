class Solution(object):
  def lengthOfLongestSubstring(self, s):
    if not s:
      return 0
    maxLen = 0
    left, d = 0, ""
    for right, char in enumerate(s):
      if char in d:
        left = left + s[left:right].find(char) + 1
      d = s[left:right + 1]
      maxLen = max(maxLen, right - left + 1)
    return maxLen
