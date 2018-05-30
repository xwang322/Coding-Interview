class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x, -n)
        elif n == 1:
            return x
        elif n == 2:
            return x**2
        else:
            temp = self.myPow(x, n/2)
            remain = n%2
            if remain:
                return temp*temp*x
            else:
                return temp*temp
