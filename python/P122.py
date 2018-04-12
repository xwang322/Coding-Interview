class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                answer += prices[i] - prices[i-1]
        return answer