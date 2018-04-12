class Solution(object):
    def magicalString(self, n):
        if n <=0:
            return 0
        s = [1,2,2]
        index = 2
        while len(s) < n:
            s += s[index]*[3-s[-1]]
            index += 1
        return s[:n].count(1)