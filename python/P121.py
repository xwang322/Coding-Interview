class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [0]*len(prices)
        minimum = float('Inf')
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            if prices[i] > minimum:
                dp[i] = prices[i] - minimum
        return max(dp)
        