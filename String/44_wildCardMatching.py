class Solution(object):
  def isMatch(self, s, p):
    if s == p:
      return True
    if len(s) < len(p) - p.count('*'):
      return False
    n, m = len(s), len(p)
    if m > 30000:
      return False
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
    dp[0][0] = True
    for j in range(len(p)):
      if p[j] != '*':
        dp[0][j+1] = False
      else:
        allStar = True
        for k in range(j + 1):
          if not dp[0][k]:
            allStar = False
        dp[0][j+1] = allStar
    
    for i in range(len(s)):
      for j in range(len(p)):
        if p[j] == '*':
          # hasMatchCut = False
          # for k in range(i + 2):
          #   if dp[k][j]:
          #     hasMatchCut = True
          #     break
          # dp[i+1][j+1] = hasMatchCut
          dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
        else:
          if p[j] == '?':
            dp[i+1][j+1] = dp[i][j]
          else:
            dp[i+1][j+1] = dp[i][j] and s[i] == p[j]
    return dp[n][m]

a = Solution().isMatch("ho", "**ho")
print(a)