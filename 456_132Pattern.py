# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
  
class Solution(object):
  def find132pattern(self, nums):
    minx = float('Inf')
    segs = []
    for x in nums:
      while segs and x >= segs[-1][1]:
        segs.pop()
      if segs and x > segs[-1][0]:
        return True
      minx = min(minx, x)
      segs.append([minx, x])
    return False