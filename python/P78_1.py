class Solution(object):
    def subsets(self, nums):
        answer = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1<<j:
                    tmp.append(nums[j])
            answer.append(tmp)
        return answer
        