class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for i in range(n)]
        for gap in range(2,n):
            for i in xrange(n-gap):
                j = i+gap
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n-1]