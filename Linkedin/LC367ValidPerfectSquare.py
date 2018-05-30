class Solution(object):
    def isPerfectSquare(self, num):
        return int(math.sqrt(num))**2 == num
