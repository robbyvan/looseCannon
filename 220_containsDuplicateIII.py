# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

class Solution(object):
  def containsNearbyAlmostDuplicate(self, nums, k, t):
    if t < 0:
      return False
    n = len(nums)
    d = {}
    width = t + 1
    for i in xrange(n):
      bucket = nums[i] / width
      if bucket in d:
        return True
      if bucket - 1 in d and abs(nums[i] -  d[bucket - 1]) < width:
        return True
      if bucket + 1 in d and abs(nums[i] -  d[bucket + 1]) < width:
        return True
      d[bucket] = nums[i]
      if i >= k
        del d[nums[i - k] / width]
    return False