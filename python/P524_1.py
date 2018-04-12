class Solution(object):
    def findLongestWord(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        return max(sorted(filter(isSubsequence, d))+[''], key = len)
