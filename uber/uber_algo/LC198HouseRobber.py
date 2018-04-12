class Solution(object):
    def rob(self, nums):
        '''
        # This method allocates 2 more space which is a little bad
        if not nums:
            return 0
        dp = [0]*(len(nums)+2)
        for i in range(2, len(nums)+2):
            dp[i] = max(nums[i-2]+dp[i-2], dp[i-1])
        return max(dp[-1], dp[-2])
        '''
        # This method no need to allocate extra space
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
