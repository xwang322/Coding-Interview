class Solution(object):
    # by typical DP method
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

class Solution(object):
    # by dp+BFS method
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        dp = [0]*len(nums)
        end = 0
        for num in nums:
            i, j = 0, end
            while i < j:
                m = (i+j)/2
                if num > dp[m]:
                    i = m+1
                else:
                    j = m
            dp[i] = num
            end = max(i+1, end)
        while dp and dp[-1] == 0:
            dp.pop()
        return len(dp)

# learnt from LC 354, above binary search is not very easy to understanding, so do it in a better way
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            elif index == 0:
                dp[0] = num
            elif dp[index] > num:
                dp[index] = num
        return len(dp)
