class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        temp1 = 1
        temp2 = 2
        for i in range(2, n):
            temp = temp2
            temp2 += temp1
            temp1 = temp
        return temp2