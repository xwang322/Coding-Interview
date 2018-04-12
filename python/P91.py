class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i+1] += dp[i]
            elif s[i] == '0' and (int(s[i-1]+s[i]) == 10 or int(s[i-1]+s[i]) == 20):
                dp[i+1] = dp[i-1]
            if 11 <= int(s[i-1]+s[i]) <= 19 or 21 <= int(s[i-1]+s[i]) <= 26:
                dp[i+1] = dp[i] + dp[i-1]
        return dp[-1]
        