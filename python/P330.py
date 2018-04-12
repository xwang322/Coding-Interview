class Solution(object):
    def minPatches(self, nums, n):
        max_num = 0
        count = 0
        i = 0
        while max_num < n:
            if i >= len(nums) or max_num < nums[i]-1:
                max_num += max_num+1
                count += 1
            else:
                max_num += nums[i]
                i += 1;
        return count