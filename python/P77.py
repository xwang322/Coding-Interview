class Solution(object):
    def combine(self, n, k):
        if n<=0 or k<=0:
            return []
        answer = []
        nums = [i+1 for i in range(n)]
        self.dfs(nums, answer, [], k, 0)
        return answer
    
    def dfs(self, nums, answer, path,  k, index):
        if len(path) == k:
            answer.append(path)
            return 
        if len(path) + len(nums[index:]) < k:
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, answer, path+[nums[i]], k, i+1)
            
                