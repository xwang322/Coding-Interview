class Solution(object):
    def rob(self, nums):
        if len(nums) < 2:
            return sum(nums)
        last1, now1 = 0, 0
        for i in range(len(nums)-1):
            last1, now1 = now1, max(last1+nums[i], now1)
        last2, now2 = 0, 0
        for i in range(len(nums)-1, 0, -1):
            last2, now2 = now2, max(last2+nums[i], now2)
        return max(now1, now2)
