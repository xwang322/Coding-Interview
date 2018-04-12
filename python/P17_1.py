class Solution(object):
    def letterCombinations(self, digits):
        dictionary = {'0':'', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        answer = ['']
        for d in digits:
            answer = [a+b for b in dictionary[d] for a in answer]
        return answer
        