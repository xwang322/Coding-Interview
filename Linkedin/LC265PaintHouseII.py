class Solution(object):
    def minCostII(self, costs):
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        dp = [[0 for i in range(k)] for j in range(n)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = min(dp[i-1][:j] + dp[i-1][j+1:]) + costs[i][j]
        return min(dp[-1][:])
        
