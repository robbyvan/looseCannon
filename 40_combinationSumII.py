# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
class Solution(object):
  def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res
  def dfs(self, candidates, target, index, path, res):
    if target < 0:
      return
    if target == 0:
      res.append(path)
      return
    for i in xrange(index, len(candidates)):
      if i != index and candidates[i] == candidates[i - 1]:
        continue
      self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)