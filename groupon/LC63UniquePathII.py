class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)]for j in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0
        for i in range(1, m):
            if dp[i-1][0] and obstacleGrid[i][0] == 0:
                dp[i][0] = 1
        for i in range(1, n):
            if dp[0][i-1] and obstacleGrid[0][i] == 0:
                dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
