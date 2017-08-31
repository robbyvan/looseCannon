class Solution(object):
  def canJump(self, nums):
    for index in xrange(len(nums) - 1, 0, -1):
      