class Solution(object):
    def trailingZeroes(self, n):
        sum_num = 0
        base = 5
        while (base <= n):
            sum_num += n/base
            base *= 5
        return sum_num