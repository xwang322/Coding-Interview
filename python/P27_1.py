class Solution(object):
    def removeElement(self, nums, val):
        length = len(nums)
        j = length-1
        for i in range(length-1, -1, -1):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return j+1