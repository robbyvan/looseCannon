# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

class Solution(object):
  def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 1

    for initIndex in xrange(len(nums)):
      curr = nums[initIndex]
      while curr > 0 and curr <= len(nums) and curr != nums[curr - 1]:
        temp = nums[curr - 1]
        nums[curr - 1] = curr
        curr = temp
    # print(nums)
    for i in xrange(len(nums)):
      if (i + 1) != nums[i]:
        return i + 1
    return len(nums) + 1

