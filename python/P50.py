class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1.0/self.myPow(x, -n)
        else:
            if n == 1:
                return x
            elif n == 2:
                return x*x
            else:
                if not n%2:
                    return self.myPow(x*x, n/2)
                else:
                    return self.myPow(x*x, n/2)*x
                    