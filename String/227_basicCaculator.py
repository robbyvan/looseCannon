class Solution(object):
  def calculate(self, s):
    if not s:
      return '0'
    stack, num, sign = [], 0, '+'
    for i in xrange(len(s)):
      if s[i].isdigit():
        num = num * 10 + ord(s[i]) - ord('0')
      if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
        if sign == '+':
          stack.append(num)
        elif sign == '-':
          stack.append(-num)
        elif sign =='*':
          stack.append(num * stack.pop())
        elif sign == '/':
          temp = stack.pop()
          if temp // num < 0 and temp % num != 0:
            stack.append(temp // num + 1) # truncate towards zero
          else:
            stack.append(temp // num)
        sign = s[i]
        num = 0
    return sum(stack)