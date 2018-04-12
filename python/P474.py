class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for s in strs:
            zero = s.count('0'); one = s.count('1')
            for x in range(m, zero-1, -1):
                for y in range(n, one-1, -1):
                    dp[x][y] = max(dp[x-zero][y-one]+1, dp[x][y])
        return dp[m][n]
        