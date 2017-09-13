class Solution(object):
  def palindromePairs(self, words):
    res = []
    if not words:
      return res

    d = {}
    for i in range(len(words)):
      d[words[i]] = i

    if "" in d:
      blankIndex = d[""]
      for i in range(len(words)):
        if (self.isPalindrome(words[i])):
          if i == blankIndex:
            continue
          res.append([blankIndex, i])
          res.append([i, blankIndex])

    for i in range(len(words)):
      curr = words[i]
      curr_r = curr[::-1]
      if curr_r in d and d[curr_r] != i:
        res.append([i, d[curr_r]])

    for i in range(len(words)):
      curr = words[i]
      for cut in range(1, len(curr)):
        if self.isPalindrome(curr[:cut]):
          curr_r = (curr[cut:])[::-1]
          if curr_r in d and d[curr_r] != i:
            res.append([d[curr_r], i])

        if self.isPalindrome(curr[cut:]):
          curr_r = (curr[:cut])[::-1]
          if curr_r in d and d[curr_r] != i:
            res.append([i, d[curr_r]])

    return res

  def isPalindrome(self, s):
    i, j = 0, len(s) - 1
    while i <= j:
      if s[i] != s[j]:
        return False
      i += 1
      j -= 1
    return True


a = Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])
print(a)