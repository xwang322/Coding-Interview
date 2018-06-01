class Solution(object):
    def minCost(self, costs):
        if not costs:
            return 0
        n = len(costs)
        dp = [[0 for i in range(3)]for j in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + costs[i][2]
        return min(dp[-1][0], dp[-1][1], dp[-1][2])


class Solution(object):
    def minCost(self, costs):
        if not costs:
            return 0
        n = len(costs)
        for i in range(1, n):
            costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
            costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
            costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]
        return min(costs[-1][0], costs[-1][1], costs[-1][2])
