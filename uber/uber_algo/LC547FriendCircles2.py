
class Solution(object):
    def findCircleNum(self, M):
        if not M:
            return 0
        n = len(M)
        visited = set()
        answer = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                self.dfs(M, n, i, visited)
                answer += 1
        return answer

    def dfs(self, M, n, i, visited):
        for j in range(n):
            if j != i and M[i][j]:
                if j not in visited:
                    visited.add(j)
                    self.dfs(M, n, j, visited)
        
