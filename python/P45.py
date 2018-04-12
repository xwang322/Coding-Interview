class Solution(object):
    def jump(self, nums):
        last, max_jump = 0, 0
        number, i = 0, 0
        while max_jump < len(nums)-1:
            while i <= last:
                max_jump = max(i+nums[i], max_jump)
                i += 1
            if last == max_jump:
                return -1
            last = max_jump
            number += 1
        return number
        