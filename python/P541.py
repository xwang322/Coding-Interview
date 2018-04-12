class Solution(object):
    def reverseStr(self, s, k):
        if not s:
            return ""
        return s[:k][::-1]+s[k:2*k] + self.reverseStr(s[2*k:], k)
        