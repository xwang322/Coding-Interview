class Solution(object):
    def findMin(self, nums):
        length = len(nums)
        if nums[0]<nums[length-1]:
            return nums[0]
        return self.findit(nums, 0, length-1)
    
    def findit(self, nums, left, right):
        if left == right:
            return nums[left]
        if left+1 == right:
            return nums[left] if nums[left] < nums[right] else nums[right]
        mid = (left+right)/2
        if nums[mid] > nums[left]:
            return self.findit(nums, mid, right)
        if nums[mid] < nums[left]:
            return self.findit(nums, left, mid)
        return nums[mid]