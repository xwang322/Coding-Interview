class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        if nums[left] < target:
            return left+1
        else:
            return left