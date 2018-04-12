class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        dic = {}
        stack = []
        answer = []
        for num in nums:
            while stack and stack[-1]<num:
                dic[stack.pop()] = num
            stack.append(num)
        for num in findNums:
            answer.append(dic.get(num, -1))
        return answer
                