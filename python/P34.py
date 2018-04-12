class Solution(object):
    def searchRange(self, nums, target):
        # easy way by Python built-in function
        if not nums or len(nums) == 0 or target not in nums:
            return [-1, -1]
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1]

                
            