class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(dp)):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[-1]