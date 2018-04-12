class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates or not target:
            return []
        candidates.sort()
        temp_list = []
        for candidate in candidates:
            if candidate <= target:
                temp_list.append(candidate)
        answer = []
        self.dfs(answer, temp_list, target, [])
        final = []
        for each in answer:
            if each not in final:
                final.append(each)
        return final

    def dfs(self, answer, candidates, target, path):
        if target < 0:
            return
        elif target == 0:
            answer.append(path)
            return
        for index, candidate in enumerate(candidates):
            self.dfs(answer, candidates[index+1:], target-candidate, path+[candidate])
