class Solution(object):
    def generateParenthesis(self, n):
        # awesome dp solution   
        dp = [[] for i in range(n+1)]
        dp[0].append('')
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += ['('+x+')'+y for x in dp[j] for y in dp[i-1-j]]
        return dp[n]