class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        if target > nums[-1] and target < nums[0]:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid-1
        return -1
