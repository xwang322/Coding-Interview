class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return []
        left = [1 for i in range(len(nums))]
        left[0] = 1
        pivot = 1
        for i in range(len(nums)-1):
            left[i+1] = nums[i]*pivot
            pivot = left[i+1]
        right = [1 for i in range(len(nums))]
        right[-1] = 1
        pivot = 1
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = nums[i]*pivot
            pivot = right[i-1]
        answer = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]
        return answer
        