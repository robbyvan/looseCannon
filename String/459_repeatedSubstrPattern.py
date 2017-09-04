# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

# Example 1:
# Input: "abab"

# Output: True

# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"

# Output: False
# Example 3:
# Input: "abcabcabcabc"

# Output: True

# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution(object):
  def repeatedSubstringPattern(self, s):
    if len(s) < 2:
      return False
    p = s[0]
    index = 1
    curr = 1
    while index + len(p) < len(s):
      if s[index : index + len(p)] == p:
        index += len(p)
      else:
        p = s[:curr + 1]
        curr += 1
        index = curr
    if s[len(s) - len(p) : len(s)] == p:
      return True
    return False
# a = Solution().repeatedSubstringPattern('abaababaab')
# print(a)


