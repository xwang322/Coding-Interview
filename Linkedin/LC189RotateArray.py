class Solution(object):
    def rotate(self, nums, k):
        if k == 0:
            return
        index = len(nums) - k
        nums[:] = nums[index:] + nums[:index] 