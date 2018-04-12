class Solution(object):
    def repeatedSubstringPattern(self, s):
        return any(s[:i]*(len(s)/i) == s for i in range(1, len(s)) if len(s)%i == 0)
        