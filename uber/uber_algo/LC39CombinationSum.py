class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        if not candidates:
            return []
        answer = []
        self.dfs(answer, [], target, candidates)
        return answer
        
    def dfs(self, answer, path, target, candidates):
        if target == 0:
            answer.append(path)
            return 
        if target < 0:
            return
        for index, candidate in enumerate(candidates):
            self.dfs(answer, path+[candidate], target-candidate, candidates[index:])
        