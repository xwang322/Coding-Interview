class Solution(object):
    def generateParenthesis(self, n):
        if not n:
            return []
        answer = []
        self.dfs(answer, n, n, '')
        return answer

    def dfs(self, answer, n1, n2, path):
        if n2 < 0 or n1 < 0:
            return
        if n2 < n1:
            return
        if n1 == n2 == 0:
            answer.append(path)
            return
        self.dfs(answer, n1-1, n2, path+'(')
        self.dfs(answer, n1, n2-1, path+')')
