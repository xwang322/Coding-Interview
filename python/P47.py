class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return []
        answer = []
        self.dfs(nums, answer, [])
        return map(list, set(map(tuple, answer)))
    
    def dfs(self, nums, answer, path):
        if len(nums) == 0:
            answer.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], answer, path+[nums[i]])
        