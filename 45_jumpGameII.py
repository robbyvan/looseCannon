# Dynamic Programming
class Solution(object):
  def jump(self, nums):
    opt = []
    opt.append(0)
    for i in range(1, len(nums)):
      reachable = False
      optJump = float('inf')
      for j in range(len(opt)):
        if j + nums[j] >= i:
          reachable = True
          optJump = min(optJump, opt[j] + 1)
      if not reachable:
        print(i, j, opt, nums)
        return False
      opt.append(optJump)
    return opt[-1]

# Greedy
class Solution(object):
  def jump(self, A):
    if not A:
      return False

    start, end, jumps = 0, 0, 0
    while end < len(A) - 1:
      jumps += 1
      farthest = end
      for i in range (start, end + 1):
        if A[i] + i > farthest:
          farthest = A[i] + i
      start = end + 1
      end = farthest
      
    return jumps
