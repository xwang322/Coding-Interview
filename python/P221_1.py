class Solution(object):
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        answer = 0
        for i in range(m):
            for j in range(n):
                if not (i and j) and int(matrix[i][j]):
                    dp[i][j] = 1
                elif (i and j) and int(matrix[i][j]):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                answer = max(answer, dp[i][j])
        return answer*answer
        