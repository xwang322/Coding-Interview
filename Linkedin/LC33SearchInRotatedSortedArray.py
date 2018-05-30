class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        if target > nums[-1] and target < nums[0]:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            if right-left <= 1:
                if target in nums[left:right+1]:
                    return left if target == nums[left] else right
                return -1
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
                
