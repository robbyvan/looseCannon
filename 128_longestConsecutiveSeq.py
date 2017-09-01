class Solution(object):
  def longestConsecutive(self, nums):
    s = set(nums)

    longest = 0
    for num in nums:
      down = num - 1
      while down in set:
        down -= 1

      up = num + 1
      while up in set:
        up += 1

      longest = Math.max(longest, up - down - 1)
    return longest