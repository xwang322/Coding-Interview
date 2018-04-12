class Solution(object):
    # DFS, TLE
    '''
    def wordBreak(self, s, wordDict):
        for char in s:
            flag = False
            for word in wordDict:
                if char in word:
                    flag = True
            if flag == False:
                return False
        return self.dfs(s, wordDict)
        
    def dfs(self, s, wordDict):
        if s in wordDict:
            return True
        for word in wordDict:
            if word == s[0:len(word)]:
                if self.dfs(s[len(word):], wordDict):
                    return True
        return False
    '''
    def wordBreak(self, s, wordDict):
        dp = [True] * (len(s)+1)
        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))
        return dp[-1]
  