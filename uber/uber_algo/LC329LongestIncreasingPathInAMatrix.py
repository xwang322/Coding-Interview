class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(matrix, dp, m, n, i, j)
        answer = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] > answer:
                    answer = dp[i][j]
        return answer

    def dfs(self, matrix, dp, m, n, i, j):
        if not dp[i][j]:
            temp = matrix[i][j]
            temp1 = self.dfs(matrix, dp, m, n, i-1, j) if i-1>=0 and temp > matrix[i-1][j] else 0
            temp2 = self.dfs(matrix, dp, m, n, i+1, j) if i+1<=m-1 and temp > matrix[i+1][j] else 0
            temp3 = self.dfs(matrix, dp, m, n, i, j-1) if j-1>=0 and temp > matrix[i][j-1] else 0
            temp4 = self.dfs(matrix, dp, m, n, i, j+1) if j+1<=n-1 and temp > matrix[i][j+1] else 0
            dp[i][j] = 1+max(temp1, temp2, temp3, temp4)
        return dp[i][j]
