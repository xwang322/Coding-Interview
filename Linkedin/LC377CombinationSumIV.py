class Solution(object):
    def combinationSum4(self, nums, target):
        if not nums:
            return 0
        nums.sort()
        dp = [0 for i in range(target+1)]
        for num in nums:
            if num <= target:
                dp[num] = 1
        for i in range(1, target+1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]]
        return dp[-1]
        