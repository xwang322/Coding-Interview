class Solution(object):
    def generateParenthesis(self, n):
        if not n:
            return []
        answer = []
        self.dfs(answer, '', 0, 0, n)
        return answer
        
    def dfs(self, answer, path, left, right, n):
        if left == right:
            if left == n:
                answer.append(path)
                return
        if left < right:
            return
        if left > n or right > n:
            return
        self.dfs(answer, path+'(', left+1, right, n)
        self.dfs(answer, path+')', left, right+1, n)
        