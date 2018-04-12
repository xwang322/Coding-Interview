class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]
        for i in range(1, len(s2)+1):
            dp[0][i] = dp[0][i-1] and s3[i-1] == s2[i-1]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s3[i-1+j] == s1[i-1]) or (dp[i][j-1] and s2[j-1] == s3[j-1+i])
        return dp[len(s1)][len(s2)]