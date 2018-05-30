class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        if target < nums[0]:
            return [-1, -1]
        elif target > nums[-1]:
            return [-1, -1]
        else:
            index1 = bisect.bisect_left(nums, target)
            index2 = bisect.bisect_right(nums, target)
            if index2 == index1:
                return [-1, -1]
            return [index1, index2-1]
        
