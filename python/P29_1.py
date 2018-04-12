class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return -1
        if dividend == 0 and divisor != 0:
            return 0
        if (dividend<0 and divisor>0) or (dividend<0 and divisor>0):
            if abs(dividend) < abs(divisor):
                return 0
        sum_temp = 0
        count = 0
        answer = 0
        a = abs(dividend)
        b = abs(divisor)
        while b <= a:
            sum_temp = b
            count = 1
            while sum_temp+sum_temp <= a:
                count += count
                sum_temp += sum_temp
            a -= sum_temp
            answer += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            answer = -answer
        if answer > 2**31-1:
            return 2**31-1
        return answer