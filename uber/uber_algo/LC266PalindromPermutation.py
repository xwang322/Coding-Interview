class Solution(object):
    def canPermutePalindrome(self, s):
        if not s:
            return True
        dictionary = collections.Counter(s)
        temp = sum(value%2 for value in dictionary.values())
        if temp >= 2:
            return False
        else:
            return True