class Solution(object):
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        answer = []
        nums.sort()
        self.dfs(nums, answer, [], 0)
        return map(list, set(map(tuple, answer)))
        
    def dfs(self, nums, answer, path, index):
        answer.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, answer, path+[nums[i]], i+1)