class Solution(object):
    def combinationSum3(self, k, n):
        answer = []
        candidates = [i+1 for i in range(9)]
        self.dfs(answer, candidates, k ,n, [])
        return answer
    
    def dfs(self, answer, candidates, k, n, path):
        if len(path) == k and sum(path) == n:
            answer.append(path)
            return 
        if len(path) > k or sum(path) > n:
            return
        for index, candidate in enumerate(candidates):
            self.dfs(answer, candidates[index+1:], k, n, path+[candidate])