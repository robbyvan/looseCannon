class Solution(object):
  def addBinary(self, a, b):
    if len(a) == 0:
      return b
    if len(b) ==0:
      return a
    if a[-1] == '1' and b[-1] == '1':
      return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
    if a[-1] == '0' and b[-1] == '0':
      return self.addBinary(a[:-1], b[:-1]) + '0'
    return self.addBinary(a[:-1], b[:-1]) + '1'

# class Solution(object):
#   def addBinary(self, a, b):
#     carry = 0
#     pa ,pb = len(a) - 1, len(b) - 1
#     res = ''
#     while pa >= 0 or pb >= 0:
#       x = int(a[pa]) if pa >= 0 else 0
#       y = int(b[pb]) if pb >= 0 else 0
#       s = x + y + carry
#       print(s)
#       res = str(s % 2) + res
#       carry = s / 2
#       pa -= 1
#       pb -= 1
#     if carry:
#       res = '1' + res
#     return res
#     