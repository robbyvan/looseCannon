class Solution(object):
  def merge(self, left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        result.append(left[i])
        i += 1
      else:
        result.append(right[j])
        j += 1
    result += left[i:]
    result += right[j:]
    return result
    
  def mergeSort(self, lists):
    if len(lists) <= 1:
      return lists
    num = len(lists) / 2
    left = mergeSort(lists[:num])
    right = mergeSort(lists[num:])
    return merge(left, right)