class Solution(object):
  def longestPalindromeSubseq(self, s):
    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in xrange(n):
      dp[i][i] = 1
    for i in xrange(n, -1, -1):
      for j in range(i + 1, n):
        if s[i] == s[j]:
          if i + 1 <= j - 1:
            dp[i][j%2] = dp[i+1][(j-1)%2] + 2
          else:
            dp[i][j%2] = 2
        else:
          dp[i][j%2] = max(dp[i+1][j%2], dp[i][(j-1)%2])
    return dp[0][-1]