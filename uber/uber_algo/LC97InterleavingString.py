class Solution(object):
    # This solution will TLE
    def isInterleave(self, s1, s2, s3):
        if not s1 or not s2:
            return s1+s2 == s3
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [False]*(len(s3)+1)
        dp[0] = True
        i = 0
        j = 0
        for k in range(len(s3)):
            if dp[k] and s3[k] == s1[i] and s3[k] != s2[j]:
                i += 1
                dp[k+1] = True
            elif dp[k] and s3[k] == s2[j] and s3[k] != s1[i]:
                j += 1
                dp[k+1] = True
            elif dp[k] and s3[k] == s2[j] == s1[i]:
                if self.isInterleave(s1[i+1:], s2[j:], s3[k+1:]):
                    i += 1
                    dp[k+1] = True
                elif self.isInterleave(s1[i:], s2[j+1:], s3[k+1:]):
                    j += 1
                    dp[k+1] = True
                else:
                    return False
            else:
                return False
            if i == len(s1):
                return s3[k+1:] == s2[j:]
            elif j == len(s2):
                return s3[k+1:] == s1[i:]
        return True

# This solution is fine
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if not s1 or not s2:
            return s1+s2 == s3
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            if dp[i-1][0] and s1[:i] == s3[:i]:
                dp[i][0] = True
        for i in range(1, len(s2)+1):
            if dp[0][i-1] and s2[:i] == s3[:i]:
                dp[0][i] = True
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
