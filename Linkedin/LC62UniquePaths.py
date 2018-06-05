class Solution(object):
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(m):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]