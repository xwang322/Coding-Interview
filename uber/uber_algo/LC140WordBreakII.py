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
            if word == s:
                answer.append(word)
            else:
                rest = self.dfs(s[len(word):], wordDict, memo)
                for item in rest:
                    # item here should refer to different subpaths
                    item = word + ' ' + item
                    answer.append(item)
        memo[s] = answer
        return answer
    '''
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        answer = []
        memo = {}
        self.dfs(s, s, wordDict, memo, [], answer)
        return answer

    def dfs(self, target, temptarget, wordDict, memo, path, answer):
        string = ''.join(path)
        if not temptarget:
            if string == target:
                for i in range(len(path)-1, -1, -1):
                    memo[''.join(path[i:])] = memo.get(''.join(path[i:]), [])+[path[i:]]
                answer.append(' '.join(path))
            return
        for word in wordDict:
            if temptarget.startswith(word):
                self.dfs(target, temptarget[len(word):], wordDict, memo, path+[word], answer)
    '''
    '''
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        answer = []
        self.dfs(answer, wordDict, [], s, s, {})
        return answer

    def dfs(self, answer, wordDict, path, temptarget, target, memo):
        if temptarget in memo:
            return memo[temptarget]
        if ''.join(path) == target:
            answer.append(' '.join(path))
            return
        if ''.join(path) not in target:
            return
        for word in wordDict:
            if temptarget.startswith(word):
                self.dfs(answer, wordDict, path+[word], temptarget[len(word):], target, memo)
    '''
