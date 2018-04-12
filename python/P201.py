class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        answer = 0
        while m != n:
            m >>= 1
            n >>= 1
            answer += 1
        return m<<answer