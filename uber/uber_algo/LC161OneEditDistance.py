class Solution(object):
    def isOneEditDistance(self, s, t):
        if s == t:
            return False
        m = len(s)
        n = len(t)
        if n < m:
            return self.isOneEditDistance(t,s)
        if abs(m-n) > 1:
            return False
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    s = s[:i]+t[i]+s[i+1:]
                else:
                    s = s[:i]+t[i]+s[i:]
                break
        return s == t or s == t[:-1]