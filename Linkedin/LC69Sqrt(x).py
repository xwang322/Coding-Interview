class Solution(object):
    def mySqrt(self, x):
        if not x:
            return 0
        if x == 1:
            return 1
        left = 1
        right = x
        while left <= right:
            mid = (left+right)/2
            if mid*mid > x:
                right = mid-1
            elif mid*mid == x:
                return mid
            else:
                left = mid+1
        answer = min(left, right)
        return answer

        
