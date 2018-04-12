class Solution(object):
    def letterCombinations(self, digits):
        if not digits or len(digits) == 0:
            return []
        dictionary = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 1:
            return [char for char in dictionary[digits[0]]]
        else:
            temp_list = dictionary[digits[0]]
            rest = self.letterCombinations(digits[1:])
            return [char1 + char2 for char1 in temp_list for char2 in rest]

        