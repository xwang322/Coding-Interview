class Solution:
    # I like this one better because it simply tell why two rounds is enough.
    def rob(self, nums):
        if len(nums) < 2:
                return sum(nums)
        def rob1(nums):
            cur = 0
            last = 0
            for i in nums:
                temp = cur
                cur = max(last+i, cur)
                last = temp
            return cur
        return max(rob1(nums[:-1]), rob1(nums[1:]))
