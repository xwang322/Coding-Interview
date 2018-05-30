class Solution(object):
    def maxSubArray(self, nums):
        answer = nums[0]
        tempsum = 0
        for num in nums:
            tempsum += num
            if tempsum > answer:
                answer = tempsum
            if tempsum < 0:
                tempsum = 0
        return answer
        
