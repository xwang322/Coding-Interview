class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return []
        answer = [1]*len(nums)
        temp = 1
        for i in range(1, len(nums)):
            answer[i] = temp*nums[i-1]
            temp = temp*nums[i-1]
        temp = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            answer[i] *= temp
            temp = nums[i]*temp
        return answer
