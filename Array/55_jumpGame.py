class Solution(object):
  def canJump(self, nums):
    maxRange = 0
    pos = 0
    for item in nums:
      if pos > maxRange:
        return False
      maxRange = max(maxRange, pos + item)
      pos += 1
    return True