class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        answer = 0
        if abs(dividend) < abs(divisor):
            return 0
        elif dividend == divisor:
            return 1
        elif dividend == -divisor:
            return -1
        else:
            temp1 = abs(dividend)
            while temp1 >= abs(divisor):
                temp2 = abs(divisor)
                temp = 1
                while temp1 >= temp2:
                    temp1 -= temp2
                    temp2 += temp2
                    answer += temp
                    temp += temp
        if (dividend > 0 and divisor > 0) or (divisor < 0 and dividend < 0):
            if answer > 2147483647:
                return 2147483647
            else:
                return answer
        elif (dividend > 0 and divisor < 0) or (divisor > 0 and dividend < 0):
            if abs(answer) >= 2147483648:
                return -2147483648
            else:
                return -answer