class Solution(object):
    def combinationSum(self, candidates, target):
        if not candidates or not target:
            return []
        candidates.sort()
        answer = []
        self.dfs(answer, candidates, target, [])
        return answer
    
    def dfs(self, answer, candidates, target, path):
        if sum(path) == target:
            answer.append(path)
            return 
        if sum(path) > target:
            return
        for index, candidate in enumerate(candidates):
            self.dfs(answer, candidates[index:], target, path+[candidate])
    