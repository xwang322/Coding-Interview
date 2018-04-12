class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        if not nums or n == 0:
            return 0
        dp = [0]*n
        dp[0] = nums[0]
        maxsum = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            maxsum = max(maxsum, dp[i])
        return maxsum
        