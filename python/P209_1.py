class Solution(object):
    def minSubArrayLen(self, s, nums):
        # sliding window
        size = len(nums)
        start, end, sum = 0, 0, 0
        bestanswer = size+1
        while True:
            if sum < s:
                if end >= size:
                    break
                sum += nums[end]
                end += 1
            else:
                if start > end:
                    break
                bestanswer = min(bestanswer, end-start)
                sum -= nums[start]
                start += 1
        return [0, bestanswer][bestanswer <= size]
                    