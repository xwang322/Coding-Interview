/*
* 问的是word break，由于时间比较久已经不记得细节了， 写完代码讨论了一下时间复杂度，和面试官解释了很久。
* word break ， 基本写出来了， 不过有两处bug
**/
def wordBreak(string, dictionary):
    dp = [False]*(len(string)+1)
    for i in range(1, len(string)+1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
    return dp[-1]

class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        answer = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                answer.append(word)
            else:
                rest = self.dfs(s[len(word):], wordDict, memo)
                for item in rest:
                    # item here should refer to different subpaths
                    item = word + ' ' + item
                    answer.append(item)
        memo[s] = answer
        return answer
