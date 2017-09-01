class Solution(object):
  def largestRectangleArea(self, height):
    if len(height) == 0:
      return 0

    if len(height) == 1:
      return height[0]

    left, right = 0, len(height) - 1
    wholeArea = min(height) * (right - left + 1)
    minIndex = height.index(min(height))
    leftPart = self.largestRectangleArea(height[:minIndex])
    rightPart = self.largestRectangleArea(height[minIndex+1:])
    maxArea = max(wholeArea, leftPart, rightPart)
    return maxArea

# a = Solution()
# c = a.largestRectangleArea([2, 1, 5, 6, 2, 3])
# print(c)