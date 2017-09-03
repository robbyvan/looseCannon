import collections
class Solution(object):
  def canConstruct(self, ransomNote, magazine):
    dr = collections.Counter(ransomNote)
    dm = collections.Counter(magazine)
    for i in dr:
      if not dm[i] or dm[i] < dr[i]:
        return False
    return True

# a = Solution().canConstruct('a', 'ccca')
# print(a)