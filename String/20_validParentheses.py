class Solution(object):
  def isValid(self, s):
    dict = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for char in s:
      if char in dict:
        stack.append(char)
      else:
        if stack and dict[stack[-1]] == char:
          stack.pop()
        else:
          return False
    if len(stack) == 0:
      return True
    return False

# class Solution(object):
#   def isValid(self, s):
#     stack = []
#     left = "([{"
#     right = ")]}"
#     for char in s:
#       if char in left:
#         stack.append(char)
#       elif char in right:
#         if char == ')':
#           if not stack or stack[-1]  != '(':
#             return False
#           else:
#             stack.pop()
#         elif char == ']':
#           if not stack or stack[-1]  != '[':
#             return False
#           else:
#             stack.pop()
#         elif char == '}':
#           if not stack or stack[-1]  != '{':
#             return False
#           else:
#             stack.pop()
#       else:
#         return False
#     if len(stack) > 0:
#       return False
#     return True