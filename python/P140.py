class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict, memo):
        if not s:
            return []
        answer = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if word == s:
                answer.append(word)
            else:
                resultofrest = self.dfs(s[len(word):], wordDict, memo)
                for each in resultofrest:
                    each = word+' '+each
                    answer.append(each)
        memo[s] = answer
        return answer