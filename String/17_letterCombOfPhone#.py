class Solution(object):
  def letterCombinations(self, digits):
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
    item, res = "", []
    self.helper(d, 0, digits, item, res)
    return res

  def helper(self, d, digitIndex, digits, item, res):
    if digitIndex > len(digits):
      return
    if digitIndex == len(digits):
      if len(digits) > 0:
        res.append(item)
      return
    digit = digits[digitIndex]
    if digit in list(d.keys()):
      chars = d[digit]
      for j in range(len(chars)):
        self.helper(d, digitIndex + 1, digits, item + chars[j], res)
    else:
      self.helper(d, digitIndex+1, digits, item, res)

  # def letterCombinations2(self, digits):
  #   if '' == digits:
  #     return []
  #   kvmaps = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
  #   return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])