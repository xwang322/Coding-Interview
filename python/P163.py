class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        def getrange(lowvalue, upvalue):
            if lowvalue == upvalue:
                return "{}".format(lowvalue)
            else:
                return "{}->{}".format(lowvalue, upvalue)
        answer = []
        pre = lower - 1
        for i in range(len(nums)+1):
            if i == len(nums):
                curr = upper+1
            else:
                curr = nums[i]
            if curr - pre >= 2:
                answer.append(getrange(pre+1, curr-1))
            pre = curr
        return answer
        