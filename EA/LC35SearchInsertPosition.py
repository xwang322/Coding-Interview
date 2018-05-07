class Solution(object):
    def searchInsert(self, nums, target):
        # return bisect.bisect_left(nums, target)
        left = 0
        right = len(nums)
        if target > nums[right-1]:
            return right
        elif target < nums[0]:
            return 0
        else:
            while True:
                if left+1 == right:
                    return left if nums[left] == target else left+1
                mid = (left+right)/2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
