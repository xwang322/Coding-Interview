class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return []
        answer = []
        nums.sort()
        self.dfs(answer, nums, [])
        final = []
        for each in answer:
            if each not in final:
                final.append(each)
        return final

    def dfs(self, answer, nums, path):
        if not nums:
            answer.append(path)
        for index, num in enumerate(nums):
            self.dfs(answer, nums[:index]+nums[index+1:], path+[num])
        
