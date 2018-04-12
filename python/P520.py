class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word[1:].islower()
        