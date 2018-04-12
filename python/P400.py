class Solution(object):
    def findNthDigit(self, n):
        start = 1
        size = 1
        step = 9
        while n > size*step:
            n -= size*step
            size += 1
            step *= 10
            start *= 10
        temp = start + (n-1)//size
        return int(str(temp)[(n-1)%size])
        
        