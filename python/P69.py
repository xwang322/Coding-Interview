class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        mid = x/2
        while left <= right:
            if mid**2 > x:
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)/2
        return mid
                