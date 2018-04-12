class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i >= 2:
                if s[i-2:i] == '20' or s[i-2:i] == '10':
                    dp[i] = dp[i-2]
                elif 11 <= int(s[i-2:i]) <= 19 or 21 <= int(s[i-2:i]) <= 26:
                    dp[i] += dp[i-2]
        return dp[-1]
        