class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1
        left = 0
        right = len(nums)-1
        while left < right:
            if right - left <= 1:
                if target <= nums[left]:
                    return left
                elif target > nums[right] and right == len(nums)-1:
                    return len(nums)
                else:
                    return right
            mid = (left+right)/2
            if nums[mid] == target:
                while nums[mid-1] == nums[mid]:
                    mid -= 1
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        # return bisect.bisect_left(nums, target)
