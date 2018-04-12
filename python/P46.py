class Solution(object):
    def permute(self, nums):
        if not nums:
            return []
        answer = []
        self.dfs(nums, answer, [])
        return answer
    
    def dfs(self, nums, answer, path):
        if len(nums) == 0:
            answer.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], answer, path+[nums[i]])
        