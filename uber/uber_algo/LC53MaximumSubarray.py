class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        cursum = nums[0]
        maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(cursum+num, num)
            maxsum = max(maxsum, cursum)
        return maxsum
