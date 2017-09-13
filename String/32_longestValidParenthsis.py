class Solution(object):
  def longestValidParentheses(self, s):
    stack = []
    left, maxLen = 0, 0
    for j in xrange(len(s)):
      if s[j] == '(':
        stack.append(j)
      else:
        if len(stack) == 0:
          left = j + 1
          continue
        stack.pop()
        if len(stack) == 0:
          maxLen = max(maxLen, j - left + 1)
        else:
          maxLen = max(maxLen, j - stack[-1])
    return maxLen
