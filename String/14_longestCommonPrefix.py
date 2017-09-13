class Solution(object):
  def longestCommonPrefix(self, strs):
    if not strs:
      return ""
    minStr = strs[0]
    for i in range(1, len(strs)):
      if len(strs[i]) < len(minStr):
        minStr = strs[i]
    last = len(minStr) - 1
    while last >= 0:
      common = True
      for i in range(0, len(strs)):
        if strs[i][0:last+1] != minStr[0:last+1]:
          last, common = last - 1, False
          break
      if not common:
        continue
      else:
        return minStr[0:last+1]
    return ""

a = Solution().longestCommonPrefix(["aca","cba"])
print(a)

# class Solution(object):
#   def longestCommonPrefix(self, strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     if not strs:
#       return ""
#     for i, letter_group in enumerate(zip(*strs)):
#       if len(set(letter_group)) > 1:
#           return strs[0][:i]
#     else:
#       return min(strs)
#         