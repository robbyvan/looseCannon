class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low, high = 0, len(nums) - 1

    while nums[low] == nums[high] and high > low:
      high -= 1

    while low < high:
      middle = low + (high - low) / 2
      if nums[middle] > nums[high]:
        low = middle + 1
      else:
        high = middle
    return nums[low]
