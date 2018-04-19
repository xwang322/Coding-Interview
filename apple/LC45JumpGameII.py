class Solution(object):
    def jump(self, nums):
        if not nums:
            return 0
        start = 0
        end = 0
        step = 0
        while end < len(nums)-1:
            step += 1
            currentmax = end+1
            for i in range(start, currentmax):
                if i + nums[i] >= len(nums)-1:
                    return step
                currentmax = max(currentmax, i+nums[i])
            start, end = end, currentmax
        return step
