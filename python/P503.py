class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        answer = [-1]*len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
        return answer
        