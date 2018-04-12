class Solution(object):
    def isPowerOfTwo(self, n):
        if not n:
            return False
        temp = bin(n)
        tmp = temp[2:]
        if tmp[0] == '1' and all(each == '0' for each in tmp[1:]):
            return True
        return False
