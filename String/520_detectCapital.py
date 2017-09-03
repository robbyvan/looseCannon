class Solution(object):
  def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()

# class Solution(object):
#   def detectCapitalUse(self, word):
#     if not word:
#       return False
#     if len(word) == 1:
#       return True
#     index = 0
#     if word[index] <= 'Z' and word[index] >= 'A':
#       index += 1
#       if word[index] <= 'Z' and word[index] >= 'A':
#         index += 1
#         for index in xrange(2, len(word)):
#           if word[index] <= 'Z' and word[index] >= 'A':
#             continue
#           return False
#         return True
#       elif word[index] <= 'z' and word[index] >= 'a':
#         index += 1
#         for index in xrange(2, len(word)):
#           if word[index] <= 'Z' and word[index] >= 'A':
#             return False
#         return True
#     elif word[index] <= 'z' and word[index] >= 'a':
#       index += 1
#       for index in xrange(1, len(word)):
#         if word[index] <= 'Z' and word[index] >= 'A':
#             return False
#       return True

# a = Solution().detectCapitalUse('USA')
# print(a)