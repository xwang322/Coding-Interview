class Solution(object):
    def partition(self, s):
        Solution.answer = []
        self.dfs(s, [])
        return Solution.answer
        
    def isvalid(self, s):
        length = len(s)
        for i in range(length):
            if s[i] != s[length-1-i]:
                return False
        return True
        
    def dfs(self, s, curr_list):
        if len(s) == 0:
            Solution.answer.append(curr_list)
        for i in range(1, len(s)+1):
            if self.isvalid(s[:i]):
                self.dfs(s[i:], curr_list+[s[:i]])
        