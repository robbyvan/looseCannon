# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.

class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low, high = 0, len(nums) - 1
    while low < high:
      middle = low + (high - low) / 2
      if nums[middle] > nums[high]:
        low = middle + 1
      else:
        high = middle
    return nums[low]
    # minVal = nums[0]
    # for num in nums:
    #   if num < minVal:
    #     return num
    # return minVal