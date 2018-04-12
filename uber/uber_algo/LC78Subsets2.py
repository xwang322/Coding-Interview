class Solution(object):
    def subsets(self, nums):
        answer = []
        self.dfs(answer, nums, [])
        return answer

    def dfs(self, answer, nums, path):
        answer.append(path)
        for index, num in enumerate(nums):
            self.dfs(answer, nums[index+1:], path+[num])
    
