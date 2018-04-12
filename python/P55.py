class Solution(object):
    def canJump(self, nums):
        if len(nums) <= 1:
            return True
        step = nums[0]
        for i in range(1, len(nums)-1):
            if step != 0:
                step -= 1
                step = max(nums[i], step)
        return step != 0