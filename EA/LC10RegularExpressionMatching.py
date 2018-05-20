class Solution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False for i in range(m+1)] for j in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[j-1] == p[i-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    if p[i-2] != '.' and p[i-2] != s[j-1]:
                        dp[i][j] = dp[i-2][j]
                    else:
                        dp[i][j] = dp[i-2][j] or dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
                
