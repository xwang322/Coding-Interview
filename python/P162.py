class Solution(object):
    '''
    def findPeakElement(self, nums):
        length = len(nums)
        return self.search(nums, 0, length-1)
        
    def search(self, nums, start, end):
        if start == end:
            return start
        if start+1 == end:
            return start if nums[start]>nums[end] else end
        mid = (start+end)/2
        if nums[mid] <= nums[mid-1]:
            return self.search(nums, start, mid-1)
        if nums[mid] <= nums[mid+1]:
            return self.search(nums, mid+1, end)
        return mid
    '''
    # writing the Java method here in Python, just for practise
    def findPeakElement(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1