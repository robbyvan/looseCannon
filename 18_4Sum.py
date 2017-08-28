# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
class Solution(object):
  def fourSum(self, nums, target):
    nums.sort()
    res = []
    length = len(nums)
    for i in range(length - 3):
      if i and nums[i] == nums[i - 1]:
        continue
      target_3 = target - nums[i]
      for j in range(i + 1, length - 2):
        if j - 1 > i and nums[j] == nums[j - 1]:
          continue
        left, right = j + 1, length - 1
        while left < right:
          s = nums[j] + nums[left] + nums[right]
          if s < target_3:
            left += 1
          elif s > target_3:
            right -= 1
          else:
            res.append([nums[i], nums[j], nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
              left += 1
            while left < right and nums[right] == nums[right - 1]:
              right -= 1
            left += 1
            right -= 1
    return res

