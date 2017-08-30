# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    d = {}
    for index, item in enumerate(nums):
      if item in d and index - d[item] <= k:
        return True
      d[item] = index
    return False
