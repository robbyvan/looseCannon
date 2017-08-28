# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Example 1:

# Input: k = 3, n = 7

# Output:

# [[1,2,4]]

# Example 2:

# Input: k = 3, n = 9

# Output:

# [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
  def combinationSum3(self, k, n):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []
    self.dfs(nums, n, k, [], res)
    return res
  def dfs(self, nums, target, step, path, res):
    if target < 0:
      return
    if step == 0:
      if target == 0:
        res.append(path)
      return
    for i in xrange (len(nums)):
      self.dfs(filter(lambda x: x > nums[i], nums), target - nums[i], step - 1, path + [nums[i]], res)