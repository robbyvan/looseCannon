class Solution(object):
  def isMatch(self, s, p):
    # if not s or not p:
    #   return False
    dp = [[False for _ in range(len(p) + 2)] for _ in range(len(s) + 1)]
    dp[0][0] = True
    dp[0][1] = True
    for j in range(len(p)):
      dp[0][j + 2] = dp[0][j] and p[j] == '*'

    for i in range(len(s)):
      for j in range(len(p)):
        if p[j] == s[i]:
          dp[i+1][j+2] = dp[i+1-1][j+2-1]
        if p[j] == '.':
          dp[i+1][j+2] = dp[i+1-1][j+2-1]
        if p[j] == '*':
          if p[j-1] != s[i] or p[j-1] != '.':
            dp[i+1][j+2] = dp[i+1][j+2-2]
          else:
            dp[i+1][j+2] = dp[i+1-1][j+2] or dp[i+1][j+2-2] or dp[i+1][j+2-1]

    return dp[-1][-1]

a = Solution().isMatch("aa", "aa")
print(a)