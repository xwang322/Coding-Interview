class Solution(object):
    def removeDuplicates(self, nums):
        if not nums or len(nums) == 1:
            return
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[start]:
                nums[start+1] = nums[i]
                start += 1
        return start +1
