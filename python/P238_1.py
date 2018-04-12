class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        left = [1] * length
        for i in range(1, length):
            left[i] = left[i-1]*nums[i-1]
        right = [1] * length
        for i in range(length-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        answer = [1]*length
        for i in range(length):
            answer[i] = left[i]*right[i]
        return answer
        
        