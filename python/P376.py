class Solution(object):
    def wiggleMaxLength(self, nums):
        size = len(nums)
        inc = dec = 1
        for x in range(1, size):
            if nums[x] > nums[x-1]:
                inc = dec+1
            elif nums[x] < nums[x-1]:
                dec = inc+1
        return max(dec, inc) if size else 0 
        