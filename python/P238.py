class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return []
        answer = [1 for i in range(len(nums))]
        for i in range(1, len(answer)):
            answer[i] = answer[i-1]*nums[i-1]
        temp = nums[-1]
        for i in range(len(answer)-2, -1, -1):
            answer[i] *= temp
            temp *= nums[i]
        return answer