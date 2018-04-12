class Solution(object):
    def singleNumber(self, nums):
        answer = 0
        for i in range(len(nums)):
            answer ^= nums[i]
        return answer