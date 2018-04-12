class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                nums[i] = nums[j+1]
                j += 1
        return j+1
        
    