class Solution(object):
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]
        answer = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if s == word:
                answer.append(word)
            else:
                rest = self.dfs(s[len(word):], wordDict, memo)
                for each in rest:
                    each = word + ' ' + each
                    answer.append(each)
        memo[s] = answer
        return answer
        
