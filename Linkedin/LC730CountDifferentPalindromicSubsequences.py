class Solution(object):
    def countPalindromicSubsequences(self, S):
        n = len(S)
        dp = [[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(1, n):
            start = 0
            end = i
            while end < n:
                if S[start] == S[end]:
                    dp[start][end] = 2*dp[start+1][end-1]
                    left = start+1
                    right = end-1
                    char = S[start]
                    while left <= right and char != S[left]:
                        left += 1
                    while left <= right and char != S[right]:
                        right -= 1
                    if left > right:
                        dp[start][end] += 2
                    elif left == right:
                        dp[start][end] += 1
                    else:
                        dp[start][end] -= dp[left+1][right-1]
                else:
                    dp[start][end] = dp[start+1][end] + dp[start][end-1] -dp[start+1][end-1]
                dp[start][end] %= 10**9+7
                end += 1
                start += 1
        return dp[0][n-1]
