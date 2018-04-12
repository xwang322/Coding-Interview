class Solution(object):
    def longestConsecutive(self, nums):
        # check if a number in set only costs O(1) time
        nums = set(nums)
        answer = 0
        for x in nums:
            y = x+1
            if x-1 not in nums:
                while y in nums:
                    y += 1
                answer = max(answer, y-x)
        return answer