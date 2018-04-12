class Solution(object):
    def combinationSum(self, candidates, target):
        if not candidates or not target:
            return []
        answer = []
        if target in candidates:
            answer.append([target])
            candidates.remove(target)
        for candidate in candidates:
            if candidate > target:
                candidates.remove(candidate)
        candidates.sort()
        self.dfs(candidates, target, answer, [], 0)
        return answer

    
    def dfs(self, candidates, target, answer, path, index):
        if target < 0:
            return 
        if target == 0:
            answer.append(path)
            return 
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], answer, path+[candidates[i]], i)
        
            
                    