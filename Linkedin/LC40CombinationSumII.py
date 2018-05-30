class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        answer = []
        self.dfs(answer, candidates, target, [])
        final = []
        for each in answer:
            if each not in final:
                final.append(each)
        return final

    def dfs(self, answer, candidates, target, path):
        if sum(path) == target:
            answer.append(path)
            return
        elif sum(path) > target:
            return
        for index, candidate in enumerate(candidates):
            self.dfs(answer, candidates[index+1:], target, path+[candidate])
        
