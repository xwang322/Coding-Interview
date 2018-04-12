class Solution(object):
    def removeDuplicates(self, nums):
        if not nums or len(nums) == 1 or len(nums) == 2:
            return
        start1 = 0
        start2 = 1
        for i in range(2, len(nums)):
            if nums[i] == nums[start1] == nums[start2]:
                pass
            elif nums[i] == nums[start2] and nums[i] != nums[start1]:
                start1 += 1
                start2 += 1
                nums[start2] = nums[i]
            elif nums[i] != nums[start2]:
                start1 += 1
                start2 += 1
                nums[start2] = nums[i]
        return start2+1
