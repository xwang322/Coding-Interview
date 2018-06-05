class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 1 if obstacleGrid[0][0] == 0 else 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(n):
            if not obstacleGrid[i][0] and dp[i-1][0]:
                dp[i][0] = 1
        for i in range(m):
            if not obstacleGrid[0][i] and dp[0][i-1]:
                dp[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]        