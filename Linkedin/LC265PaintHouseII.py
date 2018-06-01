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

# save space a little bit
class Solution(object):
    def minCostII(self, costs):
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        answer = [[0 for i in range(k)] for j in range(2)]
        for i in range(k):
            answer[0][i] = costs[0][i]
        for i in range(1, n):
            for j in range(k):
                answer[1][j] = min(answer[0][:j]+answer[0][j+1:]) + costs[i][j]
            answer[0][:] = answer[1][:]
        return min(answer[0][:])

# best solution
class Solution(object):
    def minCostII(self, costs):
        if not costs:
            return 0
        if len(costs[0]) == 1:
            return min(costs[0])
        n = len(costs)
        k = len(costs[0])
        min1 = min(costs[0])
        idx = costs[0].index(min1)
        min2 = min(costs[0][:idx] + costs[0][idx+1:])
        for i in range(1, n):
            tmin1 = float('inf')
            tmin2 = float('inf')
            tdx = -1
            for j in range(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
                if costs[i][j] <= tmin1:
                    tmin2 = tmin1
                    tmin1 = costs[i][j]
                    tdx = j
                elif costs[i][j] < tmin2:
                    tmin2 = costs[i][j]
            min1 = tmin1
            min2 = tmin2
            idx = tdx
        return min1
