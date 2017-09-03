# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
class Solution(object):
  def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    result = float("inf")
    length = len(nums)
    for i in range(length - 2):
      left, right = i + 1, length - 1
      while left < right:
        s = nums[i] + nums[left] + nums[right]
        if s == target:
          return s
        if abs(s - target) < abs(result - target):
          result = s
        if s < target:
          left += 1
        elif s > target:
          right -= 1
    return result
      

