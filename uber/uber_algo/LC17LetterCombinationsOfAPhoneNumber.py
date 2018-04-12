class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        dictionary = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        answer = []
        self.dfs(answer, '', digits, dictionary)
        return answer
    def dfs(self, answer, path, digits, dictionary):
        if not digits:
            answer.append(path)
            return 
        if digits[0]:
            for every in dictionary[digits[0]]:
                self.dfs(answer, path + every, digits[1:], dictionary)