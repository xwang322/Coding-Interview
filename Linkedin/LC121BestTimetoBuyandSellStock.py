class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        currentmin = float('inf')
        answer = float('-inf')
        for price in prices:
            currentmin = min(currentmin, price)
            answer = max(answer, price-currentmin)
        return answer
