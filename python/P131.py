class Solution(object):
    def partition(self, s):
        if not s:
            return []
        answer = []
        self.dfs(s, answer, [])
        return answer
    
    def dfs(self, s, answer, path):
        if not s:
            answer.append(path)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], answer, path+[s[:i]])
                
    def isPalindrome(self, s):
        return s == s[::-1]
        