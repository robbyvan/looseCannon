import re
class Solution(object):
  def simplifyPath(self, path):
    paths = re.split('/+', path)
    stack = []
    for ch in paths:
      if ch == '' or ch == '.':
        continue
      elif ch == '..':
        if len(stack) > 0:
          stack.pop()
      else:
        stack.append(ch)
    if len(stack) == 0:
      return '/'
    res = ''
    for folder in stack:
      res = res + '/' + folder
    return res