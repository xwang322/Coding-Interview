class Solution(object):
    def subsets(self, nums):
        if not nums:
            return []
        answer = []
        self.dfs(answer, [], nums)
        return answer
    
    def dfs(self, answer, path, nums):
        answer.append(path)
        for index, num in enumerate(nums):
            self.dfs(answer, path+[num], nums[index+1:])
        