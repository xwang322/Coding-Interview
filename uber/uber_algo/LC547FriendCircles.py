class Solution(object):
    def findCircleNum(self, M):
        if not M:
            return 0
        visited = set()
        n = len(M)
        answer = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                self.dfs(M, i, visited)
                answer += 1
        return answer

    def dfs(self, M, person, visited):
        for i in range(len(M)):
            if i != person and M[person][i]:
                if i not in visited:
                    visited.add(i)
                    self.dfs(M, i, visited)
