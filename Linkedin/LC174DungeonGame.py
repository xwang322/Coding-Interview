class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(m-2, -1, -1):
            dp[i][-1] = max(1, 1-dungeon[i][-1], dp[i+1][-1]-dungeon[i][-1])
        for i in range(n-2, -1, -1):
            dp[-1][i] = max(1, 1-dungeon[-1][i], dp[-1][i+1]-dungeon[-1][i])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1, 1-dungeon[i][j])
        return dp[0][0]
