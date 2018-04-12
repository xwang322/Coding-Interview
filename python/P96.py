class Solution(object):
    def numTrees(self, n):
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]
            for i in range(3, n+1):
                for j in range(i):
                    dp[i] += dp[j] * dp[i-1-j]
        return dp[n]