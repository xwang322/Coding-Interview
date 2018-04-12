class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1]
        
