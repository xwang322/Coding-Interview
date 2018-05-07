class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1 or n == 2:
            return n
        temp1 = 1
        temp2 = 2
        for i in range(2, n):
            temp3 = temp2
            temp2 += temp1
            temp1 = temp3
        return temp2

'''
如何更快比如 O(log n)，用矩阵power iteration
F(n) = A F(n-1)
where F(1) = [1; 1]  A = [1 1; 1 0]
Fn = [fib(n); fib(n-1)]
F(n) =  A^{n-1} * F(1)

再快, fibonacci数列有analytical solution可以O(1)求到。
The Fibonacci numbers occur in the sums of "shallow" diagonals in Pascal's triangle
