class Solution(object):
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        if n == 1:
            return True
        while n>1:
            if n%3:
                return False
            n/=3
        return True
